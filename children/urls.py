from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChildViewSet, NeonatalHealthViewSet, InfantChildHealthViewSet

router = DefaultRouter()
router.register(r'children', ChildViewSet)
router.register(r'neonatal_health', NeonatalHealthViewSet)
router.register(r'infant_child_health', InfantChildHealthViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
