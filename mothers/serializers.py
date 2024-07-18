from rest_framework import serializers
from .models import Mother, AntenatalCare, ObstetricHistory, LaborDelivery, PostnatalCare

class MotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mother
        fields = '__all__'

class AntenatalCareSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntenatalCare
        fields = '__all__'

class ObstetricHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ObstetricHistory
        fields = '__all__'

class LaborDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = LaborDelivery
        fields = '__all__'

class PostnatalCareSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostnatalCare
        fields = '__all__'
