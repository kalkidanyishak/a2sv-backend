from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyorViewSet

router = DefaultRouter()
router.register(r'surveyors', SurveyorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
