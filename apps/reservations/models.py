from django.db import models
from django.core.exceptions import ValidationError
from datetime import timedelta
from decimal import Decimal

# Create your models here.

class Reservation(models.Model):
    client = models.ForeignKey(
        "clients.Client", 
        on_delete       =models.PROTECT, 
        related_name    ="reservations",
        verbose_name    ="Cliente"
    )

    vehicle = models.ForeignKey(
        "vehicles.Vehicle", 
        on_delete       =models.PROTECT, 
        related_name    ="reservations",
        verbose_name    ="Veículo"
    )

    employee = models.ForeignKey(
        "employees.Employee",
        on_delete       =models.PROTECT,
        related_name    ="reservations",
        verbose_name    ="Funcionário"
    )

    protection = models.ForeignKey(
        "protections.Protection",
        on_delete       =models.PROTECT,
        related_name    ="reservations",
        verbose_name    ="Proteção"
    )

    created_at = models.DateTimeField("Criada em", auto_now_add=True)
    expected_pickup = models.DateTimeField("Retirada prevista")
    expected_return = models.DateTimeField("Devolução prevista")

    class Status(models.TextChoices):
        CONFIRMED = "CONFIRMADA", "confirmada"
        CANCELLED = "CANCELADA", "cancelada"
        FULFILLED = "ATENDIDA", "atendida"

    status = models.CharField(
        "situação",
        max_length=20,
        choices=Status.choices,
        default=Status.CONFIRMED,
        editable=False
    )

    notes = models.TextField("Observações", blank=True)

    contracted_daily_rate = models.DecimalField("Diária contratada", max_digits=10, decimal_places=2, default=0, editable=False, db_column="daily_rate")
    contracted_protection_rate = models.DecimalField("Proteção contratada", max_digits=10, decimal_places=2, default=0, editable=False, db_column="protection_rate")
    contracted_deductible = models.DecimalField("Franquia contratada", max_digits=10, decimal_places=2, default=0, editable=False, db_column="deductible_amount")
    estimated_total = models.DecimalField("Total estimado", max_digits=10, decimal_places=2, default=0, editable=False)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-id"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(expected_return__gt=models.F("expected_pickup")),
                name="res_return_after_pickup",
            )
        ]

    def __str__(self):
        return f"Reserva {self.pk} - {self.client}"

    def clean(self):
        super().clean()
        if self.expected_pickup and self.expected_return:
            if self.expected_return <= self.expected_pickup:
                raise ValidationError({
                    "expected_return": "A data de devolução deve ser posterior à data de retirada."
                })

    def update_prices(self, previous):
        if previous is None or previous.vehicle.id != self.vehicle.id:
            self.contracted_daily_rate = self.vehicle.vehicle_model.category.default_daily_rate
        else: 
            self.contracted_daily_rate = previous.contracted_daily_rate

        if previous is not None and previous.protection.id == self.protection.id:
            self.contracted_protection_rate = previous.contracted_protection_rate
            self.contracted_deductible = previous.contracted_deductible
        elif self.protection_id:
            self.contracted_protection_rate = self.protection.daily_rate
            self.contracted_deductible = self.protection.deductible
        else:
            self.contracted_protection_rate = Decimal("0.00")
            self.contracted_deductible = Decimal("0.00")

        if min(self.contracted_daily_rate, self.contracted_protection_rate, self.contracted_deductible) < 0:
            raise ValidationError("Diária, proteção e franquia devem ter valores não negativos.")

        duration = self.expected_return - self.expected_pickup
        days, remainder = divmod(duration, timedelta(days=1))
        if remainder:
            days += 1
        self.estimated_total = days * (self.contracted_daily_rate + self.contracted_protection_rate)

