from rest_framework     import viewsets
from inspections.models import Payment
from .serializers       import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset         = Payment.objects.all()
    serializer_class = PaymentSerializer
