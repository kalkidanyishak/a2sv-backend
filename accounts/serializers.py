# myapp/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import AdminProfile, SurveyorProfile, ClientProfile

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=[('admin', 'Admin'), ('surveyor', 'Surveyor'), ('client', 'Client')], write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role')

    def create(self, validated_data):
        role = validated_data.pop('role')
        user = User.objects.create_user(**validated_data)
        if role == 'admin':
            AdminProfile.objects.create(user=user)
        elif role == 'surveyor':
            SurveyorProfile.objects.create(user=user)
        elif role == 'client':
            ClientProfile.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
