from django.db import models

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

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-id"]

    def __str__(self):
        return f"Reserva {self.pk} - {self.client}"
