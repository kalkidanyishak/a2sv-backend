from rest_framework import viewsets
from .models import Mother, AntenatalCare, ObstetricHistory, LaborDelivery, PostnatalCare
from .serializers import MotherSerializer, AntenatalCareSerializer, ObstetricHistorySerializer, LaborDeliverySerializer, PostnatalCareSerializer

class MotherViewSet(viewsets.ModelViewSet):
    queryset = Mother.objects.all()
    serializer_class = MotherSerializer

class AntenatalCareViewSet(viewsets.ModelViewSet):
    queryset = AntenatalCare.objects.all()
    serializer_class = AntenatalCareSerializer

class ObstetricHistoryViewSet(viewsets.ModelViewSet):
    queryset = ObstetricHistory.objects.all()
    serializer_class = ObstetricHistorySerializer

class LaborDeliveryViewSet(viewsets.ModelViewSet):
    queryset = LaborDelivery.objects.all()
    serializer_class = LaborDeliverySerializer

class PostnatalCareViewSet(viewsets.ModelViewSet):
    queryset = PostnatalCare.objects.all()
    serializer_class = PostnatalCareSerializer
