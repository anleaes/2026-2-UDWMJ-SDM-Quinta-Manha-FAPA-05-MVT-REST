from django.shortcuts import render, redirect, get_object_or_404
from datetime import timedelta
from django.apps import apps
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils import timezone
from django.db.models.functions import Coalesce
from django.db import transaction
from django.contrib.auth.decorators import login_required

from maintenance.models import Maintenance
from .models import Reservation
from cnhs.models import CNH
from vehicles.models import Vehicle
from core.forms import Forms
from .forms import ReservationForm

# Create your views here.

CAR_LICENSES = ("A", "B", "AB", "C", "D", "E")
pages = Forms(Reservation, ReservationForm, "reservations", "reservation")

def check_schedule(reservation):
    start = reservation.expected_pickup
    end = reservation.expected_return
    vehicle_id = reservation.vehicle_id

    other_reservations = Reservation.objects.filter(
        vehicle_id              =vehicle_id,
        status                  =Reservation.Status.CONFIRMED,  
        expected_pickup__lt     =end,
        expected_return__gt     =start
    ).exclude(pk=reservation.pk)

    if other_reservations.exists():
        raise ValidationError("O veículo já está reservado no período solicitado.")

    first_day = timezone.localtime(start)
    last_day = timezone.localtime(end - timedelta(microseconds=1))

    maintenance = Maintenance.objects.filter(vehicle_id=vehicle_id).exclude(Q(status__iexact="CANCELADA") | Q(status__iexact="CANCELADO")).annotate(
        starts=Coalesce('actual_start', 'expected_start'),
        ends=Coalesce('actual_end', 'expected_end')
    )

    ongoing = Q(actual_start__isnull=False, actual_end__isnull=True)

    if maintenance.filter(starts__lte=last_day).filter(Q(ends__gte=first_day) | ongoing).exists():
            raise ValidationError("O veículo está em manutenção nesse período.")

    if apps.is_installed("rentals"):
        Rental = apps.get_model("rentals", "Rental")
        open_rentals = Rental.objects.filter(
            reservation__vehicle_id=vehicle_id,
            actual_return__isnull=True,
        )

        if open_rentals.filter(reservation__expected_return__lt=timezone.now()).exists():
            raise ValidationError("O veículo selecionado possui uma locação em atraso e ainda não foi devolvido ao estoque.")

        if open_rentals.filter(
            actual_pickup__lt=end,
            reservation__expected_return__gt=start,
        ).exists():
            raise ValidationError("O veículo selecionado já está locado nesse período.")

@transaction.atomic
def confirm_reservation(reservation):
    previous = None

    if reservation.pk:
        previous = Reservation.objects.select_for_update().get(pk=reservation.pk)
        if previous.status != Reservation.Status.CONFIRMED:
            raise ValidationError("A reserva não pode ser confirmada, pois não está no status 'CONFIRMADA'.")

    reservation.vehicle = Vehicle.objects.select_for_update().get(pk=reservation.vehicle_id)
    reservation.status = Reservation.Status.CONFIRMED
    reservation.clean()

    if not reservation.client.is_active or not reservation.vehicle.is_active:
        raise ValidationError("Selecione um cliente e um veículo ativos para confirmar a reserva.")

    if not reservation.employee.isactive:
        raise ValidationError("O funcionário que está confirmando a reserva deve estar ativo.")

    changed_protection = previous is None or previous.protection_id != reservation.protection_id

    if reservation.protection_id and changed_protection and not reservation.protection.is_active:
        raise ValidationError("A proteção selecionada não está ativa.")

    if not CNH.allows_rental(
        client=reservation.client,
        accepted_categories=CAR_LICENSES,
        return_date=timezone.localtime(reservation.expected_return)
    ):

        raise ValidationError("O cliente não possui CNH válida para o período da reserva.")

    check_schedule(reservation)
    reservation.update_prices(previous)
    reservation.full_clean()
    reservation.save()

def cancel_booking(reservation):
    updated = Reservation.objects.filter(
        pk=reservation.pk,
        status=Reservation.Status.CONFIRMED
    ).update(status=Reservation.Status.CANCELLED)

    if not updated:
        reservation.refresh_from_db(fields=["status"])
        if reservation.status != Reservation.Status.CONFIRMED:
            raise ValidationError("A reserva não pode ser cancelada, pois não está no status 'CONFIRMADA'.")
 
def _save_reservation(request, instance=None):
    form = ReservationForm(request.POST, instance=instance)

    if form.is_valid():
        try:
            confirm_reservation(form.save(commit=False))
        except ValidationError as error:
            form.add_error(None, error.messages)
        else:
            return redirect(pages.templates.url)

    return render(request, pages.templates.add, {"form": form})


@login_required
def add_reservation(request):
    if request.method == "POST":
        return _save_reservation(request)

    return pages.add(request)