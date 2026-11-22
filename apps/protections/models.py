from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator

# Create your models here.

class Protection(models.Model):
    name = models.CharField("Nome", max_length=50)
    description = models.TextField("Descrição")
    daily_rate = models.DecimalField(
        "Valor Diário em R$",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
    )

    class Meta:
        verbose_name = "Proteção"
        verbose_name_plural = "Proteções"
        ordering = ["id"]

    def __str__(self):
        return self.name