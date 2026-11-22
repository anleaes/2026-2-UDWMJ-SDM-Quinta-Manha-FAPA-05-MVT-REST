from django.db import models

# Create your models here.

class Protection(models.Model):
    name = models.CharField("Nome", max_length=50)
    description = models.TextField("Descrição")

    class Meta:
        verbose_name = "Proteção"
        verbose_name_plural = "Proteções"
        ordering = ["id"]

    def __str__(self):
        return self.name