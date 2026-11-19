from django.db import models

# Create your models here.
class Payment(models.Model):
    cost       = models.FloatField("Valor", null = True, blank = True, default = 0.0)
    # NOTE: Use choices?
    type       = models.CharField("Forma", max_length = 50)
    # NOTE: Use boolean?
    status     = models.CharField("Status", max_length = 50)
    created_at = models.DateField("Registrado Em", auto_now_add = True)
    approved   = models.DataField("Confirmado Em", auto_now = False, auto_now_add = False)
    receipt    = models.FileField("Comprovante", upload_to = "receipts/", null = True, blank = True)

    class Meta:
        verbose_name        = "Pagamento"
        verbose_name_plural = "Pagamentos"
        ordering            = [ "id" ]
