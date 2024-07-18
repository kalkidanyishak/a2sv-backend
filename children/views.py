from rest_framework import viewsets
from .models import Child, NeonatalHealth, InfantChildHealth
from .serializers import ChildSerializer, NeonatalHealthSerializer, InfantChildHealthSerializer

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class NeonatalHealthViewSet(viewsets.ModelViewSet):
    queryset = NeonatalHealth.objects.all()
    serializer_class = NeonatalHealthSerializer

class InfantChildHealthViewSet(viewsets.ModelViewSet):
    queryset = InfantChildHealth.objects.all()
    serializer_class = InfantChildHealthSerializer
