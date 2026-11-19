from django.db import models

# Create your models here.
class Payment(models.Model):
    cost       = models.FloatField("Valor", null = True, blank = True, default = 0.0)
    # NOTE: Use choices?
    type       = models.CharField("Forma", max_length = 50)
    # NOTE: Use boolean?
    status     = models.CharField("Status", max_length = 50)
