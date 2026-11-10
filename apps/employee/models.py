from django.db import models

# Create your models here.
class Employee(models.Model):
    name         = models.CharField("Nome", max_length = 50)
    registration = models.CharField("Matrícula", max_length = 50)
    email        = models.EmailField("E-mail", null = False, blank = False)
    phone        = models.CharField("Telefone", max_length = 20)
    approval     = models.DateField("Data de Aprovação", auto_now = False, auto_now_add = False)
    isactive     = models.BooleanField("Ativo", default = False)

