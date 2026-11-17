from django.urls    import path
from django.urls    import include
from .              import views
from rest_framework import routers

app_name = "api_maintenance"

router = routers.SimpleRouter()
router.register("", views.MaintenanceViewSet, basename = "manutencoes")
