from rest_framework import serializers
from .models import Child, NeonatalHealth, InfantChildHealth

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

class NeonatalHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeonatalHealth
        fields = '__all__'

class InfantChildHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfantChildHealth
        fields = '__all__'
