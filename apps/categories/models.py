from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField("Nome", max_length=50)
    description = models.TextField("Descrição")
    default_daily_rate = models.DecimalField("Valor Padrão da Diária", max_digits=10, decimal_places=2)
    is_active = models.BooleanField("Ativa", default=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["id"]

    def __str__(self):
        return self.name