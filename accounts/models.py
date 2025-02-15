from django.contrib.auth.models import User
from django.db import models

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class SurveyorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)