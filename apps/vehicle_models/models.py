from django.db import models
from brands.models import Brand
from categories.models import Category
from django.core.validators import MinValueValidator

# Create your models here.

class VehicleModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name="Marca")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Categoria")
    name = models.CharField("Nome", max_length=50)
    engine = models.CharField("Motor", max_length=50)
    transmission = models.CharField("Transmissão", max_length=50)
    seats = models.PositiveIntegerField("Assentos", validators=[MinValueValidator(1)])
    average_km_per_liter = models.DecimalField("Consumo Médio (km/l)", max_digits=5, decimal_places=2, validators=[MinValueValidator(0.0)])
    is_active = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Modelo de Veículo"
        verbose_name_plural = "Modelos de Veículos"
        ordering = ['name']

    def __str__(self):
        return self.name