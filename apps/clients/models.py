from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True, validators=[RegexValidator(r"\A[0-9]{11}\Z",),], help_text="CPF deve conter apenas os números. Não coloque pontos ou traços.")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        return self.name