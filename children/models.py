from django.db import models
from accounts.models import SurveyorProfile

from mothers.models import Mother

class Child(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name='children')
    surveyor = models.ForeignKey(SurveyorProfile, on_delete=models.SET_NULL, null=True, related_name='children')
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    birth_weight = models.FloatField()
    birth_length = models.FloatField()
    location=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class NeonatalHealth(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='neonatal_health')
    surveyor = models.ForeignKey(SurveyorProfile, on_delete=models.SET_NULL, null=True, related_name='neonatal_health')
    apgar_score = models.CharField(max_length=10)
    newborn_screening_results = models.TextField()
    congenital_conditions = models.TextField()
    location=models.CharField(max_length=200)

    def __str__(self):
        return f'Neonatal Health - {self.child.name}'

class InfantChildHealth(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='infant_child_health')
    surveyor = models.ForeignKey(SurveyorProfile, on_delete=models.SET_NULL, null=True, related_name='infant_child_health')
    checkup_date = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()
    head_circumference = models.FloatField()
    developmental_milestones = models.TextField()
    immunizations = models.TextField()
    nutrition = models.TextField()
    location=models.CharField(max_length=200)

    def __str__(self):
        return f'Infant and Child Health - {self.child.name} on {self.checkup_date}'
