from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MotherViewSet, AntenatalCareViewSet, ObstetricHistoryViewSet, LaborDeliveryViewSet, PostnatalCareViewSet

router = DefaultRouter()
router.register(r'mothers', MotherViewSet)
router.register(r'antenatal_care', AntenatalCareViewSet)
router.register(r'obstetric_history', ObstetricHistoryViewSet)
router.register(r'labor_delivery', LaborDeliveryViewSet)
router.register(r'postnatal_care', PostnatalCareViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
