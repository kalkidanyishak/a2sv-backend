# myapp/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import AdminProfile, SurveyorProfile, ClientProfile

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role')

    def get_role(self, obj):
        if hasattr(obj, 'adminprofile'):
            return 'admin'
        elif hasattr(obj, 'surveyorprofile'):
            return 'surveyor'
        elif hasattr(obj, 'clientprofile'):
            return 'client'
        return None

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
