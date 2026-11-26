from django.shortcuts import render
from datetime import timedelta
from django.apps import apps
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils import timezone
from django.db.models.functions import Coalesce

from maintenance.models import Maintenance
from .models import Reservation

# Create your views here.

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