from rest_framework     import serializers
from maintenance.models import Maintenance

class MaintenanceSerializer(serializers.MaintenanceSerializer):
    class Meta:
        model  = Maintenance
        fields = "__all__"
