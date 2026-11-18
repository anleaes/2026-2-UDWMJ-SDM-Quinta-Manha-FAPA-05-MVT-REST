from django.urls    import path
from django.urls    import include
from .              import views
from rest_framework import routers

app_name = "api_inspections"

router = routers.SimpleRouter()
router.register("", views.InspectionViewSet, basename = "locacoes")

urlpatterns = [
    path("", include(router.urls)),
]
