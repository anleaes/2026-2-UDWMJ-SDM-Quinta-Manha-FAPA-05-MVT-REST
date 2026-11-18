from django.db import models

# Create your models here.
class Inspection(models.Model):
    gas_fee            = models.FloatField("Taxa de Combustível", null = True, blank = True, default = 0.0)
    damage_fee         = models.FloatField("Taxa Avarias", null = True, blank = True, default = 0.0)
    fees_justification = models.TextField("Taxas Justificativas", max_length = 100)
    final_cost         = models.FloatField("Valor Final", null = True, blank = True, default = 0.0)
    # NOTE: Should this be a boolean?
    status             = models.CharField("Status", max_length = 50)
    contract           = models.FileField("Contrato", upload_to = "contracts/", null = True, blank = True)

    class Meta:
        verbose_name        = "Locação"
        verbose_name_plural = "Locações"
        ordering            = [ "id" ]
