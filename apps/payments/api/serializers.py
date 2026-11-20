from rest_framework     import serializers
from inspections.models import Payment

class PaymentSerializer(serializers.ModelSerializer):
     class Meta:
         model  = Payment
         fields = "__all__"
