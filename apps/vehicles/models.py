import re

from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Vehicle(models.Model):
    vehicle_model = models.ForeignKey("vehicleModel.VehicleModel", on_delete=models.PROTECT, related_name="vehicles", verbose_name="Modelo do Veículo")
    plate = models.CharField("Placa", max_length=7, unique=True, validators=[RegexValidator(r"\A[A-Z]{3}[0-9][A-Z0-9][0-9]{2}\Z", "A placa deve estar no formato ABC-1234 ou ABC1D23.")])
    renavam = models.CharField("Renavam", max_length=11, unique=True, validators=[RegexValidator(r"\A[0-9]+\Z", "Use somente números.")])

    class Meta: 
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
        ordering = ["vehicle_model"]

    def __str__(self):
        return f"{self.vehicle_model} - {self.plate}"