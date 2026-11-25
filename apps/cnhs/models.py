from django.db import models
from django.core.validators import RegexValidator
from pathlib import Path
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your models here.

def cnh_storage():
    return FileSystemStorage(location=Path(settings.BASE_DIR) / "private_media")
class CNH(models.Model):
    client = models.OneToOneField("clients.Client", on_delete=models.PROTECT, related_name="cnh", verbose_name="Cliente")
    number = models.CharField("Número de Registro", max_length=11, unique=True, validators=[RegexValidator(r"\A[0-9]{11}\Z", "Informe os 11 dígitos da CNH")])
    category = models.CharField("Categoria", max_length=2, choices=[("A", "A"), ("B", "B"), ("AB", "AB"), ("C", "C"), ("D", "D"), ("E", "E")])
    expiration_date = models.DateField("Data de Validade")
    document = models.FileField("Arquivo da CNH", upload_to="cnhs/", storage=cnh_storage)

    class Meta:
        verbose_name = "CNH"
        verbose_name_plural = "CNHs"
        ordering = ["id"]

    def __str__(self):
        return f"{self.client} - {self.number}"

    @classmethod
    def allows_rental(cls, *, client, accepted_categories, return_date):
        return cls.objects.filter(
            client                  =client, 
            category__in            =accepted_categories, 
            expiration_date__gte    =return_date
        ).exists()