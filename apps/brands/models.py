from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country_origin = models.CharField("País de Origem", max_length=50)
    description = models.TextField("Descrição")
    is_active = models.BooleanField("Ativo", default=True)
    logo = models.ImageField("Logo")

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ["name"]

    def __str__(self):
        return self.name