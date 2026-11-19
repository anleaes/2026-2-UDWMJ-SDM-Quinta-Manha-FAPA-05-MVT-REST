from django.db        import models
from employees.models import Employee
import os

# Create your models here.
# TODO: Add foreign key for Vehicle
class Maintenance(models.Model):
    desc           = models.TextField("Descrição", max_length = 100)
    type           = models.CharField("Tipo", max_length = 50)
    expected_start = models.DateField("Início Previsto", auto_now = False, auto_now_add = False)
    expected_end   = models.DateField("Fim Previsto", auto_now = False, auto_now_add = False)
    actual_start   = models.DateField("Início Real", auto_now = False, auto_now_add = False, null = True, blank = True)
    actual_end     = models.DateField("Fim Real", auto_now = False, auto_now_add = False, null = True, blank = True)
    cost           = models.FloatField("Custo", null = True, blank = True, default = 0.0)
    # NOTE: Should this be a boolean?
    status         = models.CharField("Status", max_length = 50)
    reports        = models.FileField("Laudo", upload_to = "reports/", null = True, blank = True)
    # NOTE: Allow null?
    employee       = models.ForeignKey(Employee, on_delete = models.CASCADE)

    class Meta:
        verbose_name        = "Manutenção"
        verbose_name_plural = "Manutenções"
        ordering            = [ "id" ]

    # NOTE: Report name without path and extension
    @property
    def reports_name(self):
        return os.path.splitext(os.path.basename(self.reports.name))[0]

    def __str__(self):
        return f"{self.desc}"
