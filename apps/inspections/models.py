from django.db           import models
from employees.models    import Employee
from reservations.models import Reservation

# Create your models here.
class Inspection(models.Model):
    pickup_date        = models.DateField("Retirada", auto_now = False, auto_now_add = False)
    return_date        = models.DateField("Devolução", auto_now = False, auto_now_add = False)
    gas_fee            = models.FloatField("Taxa de Combustível", null = True, blank = True, default = 0.0)
    damage_fee         = models.FloatField("Taxa Avarias", null = True, blank = True, default = 0.0)
    fees_justification = models.TextField("Taxas Justificativas", max_length = 100)
    final_cost         = models.FloatField("Valor Final", null = True, blank = True, default = 0.0)
    status             = models.CharField("Status", max_length = 3, choices = [
        ("CON", "Confirmada"),
        ("CAN",  "Cancelada"),
        ("ATE",   "Atendida"),
    ])
    contract           = models.FileField("Contrato", upload_to = "contracts/", null = True, blank = True)
    opened_by          = models.ForeignKey(Employee, verbose_name = "Aberto Por", on_delete = models.PROTECT, related_name = "pending_inspections")
    closed_by          = models.ForeignKey(Employee, verbose_name = "Encerrado Por", on_delete = models.PROTECT, null = True, blank = True, related_name = "finished_inspections")
    reservation        = models.OneToOneField(Reservation, verbose_name = "Reserva", on_delete = models.CASCADE, null = True, blank = True)

    class Meta:
        verbose_name        = "Locação"
        verbose_name_plural = "Locações"
        ordering            = [ "id" ]

    def __str__(self):
        return f"{self.reservation} - {self.opened_by}"
