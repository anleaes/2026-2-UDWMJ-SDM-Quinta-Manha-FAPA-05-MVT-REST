from django.db import models
from django.core.exceptions import ValidationError

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
