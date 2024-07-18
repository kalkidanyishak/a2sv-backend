from rest_framework import viewsets
from .models import Surveyor
from .serializers import SurveyorSerializer

class SurveyorViewSet(viewsets.ModelViewSet):
    queryset = Surveyor.objects.all()
    serializer_class = SurveyorSerializer
