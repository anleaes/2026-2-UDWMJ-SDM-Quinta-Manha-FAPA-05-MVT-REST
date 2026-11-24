from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class CNH(models.Model):
    client = models.OneToOneField("clients.Client", on_delete=models.PROTECT, related_name="cnh", verbose_name="Cliente")
    number = models.CharField("Número de Registro", max_length=11, unique=True, validators=[RegexValidator(r"\A[0-9]{11}\Z]", "Informe os 11 dígitos da CNH")])
    category = models.CharField("Categoria da CNH", max_length=5)

    class Meta:
        verbose_name = "CNH"
        verbose_name_plural = "CNHs"
        ordering = ["id"]

    def __str__(self):
        return f"{self.client} - {self.number}"