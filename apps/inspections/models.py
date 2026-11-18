from django.db       import models
from employee.models import Employee

# Create your models here.
class Inspection(models.Model):
    pickup_date        = models.DateField("Retirada", auto_now = False, auto_now_add = False)
    return_date        = models.DateField("Devolução", auto_now = False, auto_now_add = False)
    gas_fee            = models.FloatField("Taxa de Combustível", null = True, blank = True, default = 0.0)
    damage_fee         = models.FloatField("Taxa Avarias", null = True, blank = True, default = 0.0)
    fees_justification = models.TextField("Taxas Justificativas", max_length = 100)
    final_cost         = models.FloatField("Valor Final", null = True, blank = True, default = 0.0)
    # NOTE: Should this be a boolean?
    status             = models.CharField("Status", max_length = 50)
    contract           = models.FileField("Contrato", upload_to = "contracts/", null = True, blank = True)
    # NOTE: Should this allow null?
    employee           = models.ForeignKey(Employee, on_delete = models.CASCADE)

    class Meta:
        verbose_name        = "Locação"
        verbose_name_plural = "Locações"
        ordering            = [ "id" ]

    def __str__(self):
        return f"{self.fees_justification}"
