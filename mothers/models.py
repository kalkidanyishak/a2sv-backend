from django.db import models
from accounts.models import SurveyorProfile


class Mother(models.Model):
    surveyor = models.ForeignKey(SurveyorProfile, on_delete=models.SET_NULL, null=True, related_name='mothers')
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    marital_status = models.CharField(max_length=50)
    education_level = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    socioeconomic_status = models.CharField(max_length=100)
    residence = models.CharField(max_length=100)
    location=models.CharField(max_length=200)


    def __str__(self):
        return self.name

class AntenatalCare(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name='antenatal_care')
    surveyor = models.ForeignKey(SurveyorProfile, on_delete=models.SET_NULL, null=True, related_name='antenatal_care')
    visit_date = models.DateField()
    blood_pressure = models.CharField(max_length=10)
    weight = models.FloatField()
    hemoglobin_level = models.FloatField()
    screening_results = models.TextField()
    immunizations = models.TextField()
    location=models.CharField(max_length=200)

    def __str__(self):
        return f'Antenatal Care - {self.mother.name} on {self.visit_date}'

class ObstetricHistory(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name='obstetric_history')
    surveyor = models.ForeignKey(SurveyorProfile, on_delete=models.SET_NULL, null=True, related_name='obstetric_history')
    previous_pregnancies = models.PositiveIntegerField()
    live_births = models.PositiveIntegerField()
    stillbirths = models.PositiveIntegerField()
    miscarriages = models.PositiveIntegerField()
    complications = models.TextField()
    location=models.CharField(max_length=200)

    def __str__(self):
        return f'Obstetric History - {self.mother.name}'

class LaborDelivery(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name='labor_delivery')
    surveyor = models.ForeignKey(SurveyorProfile, on_delete=models.SET_NULL, null=True, related_name='labor_delivery')
    delivery_date = models.DateField()
    place_of_delivery = models.CharField(max_length=100)
    type_of_delivery = models.CharField(max_length=100)
    birth_attendant = models.CharField(max_length=100)
    complications = models.TextField()
    location=models.CharField(max_length=200)

    def __str__(self):
        return f'Labor and Delivery - {self.mother.name} on {self.delivery_date}'

class PostnatalCare(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name='postnatal_care')
    surveyor = models.ForeignKey(SurveyorProfile, on_delete=models.SET_NULL, null=True, related_name='postnatal_care')
    visit_date = models.DateField()
    health_assessment = models.TextField()
    breastfeeding_support = models.TextField()
    location=models.CharField(max_length=200)

    def __str__(self):
        return f'Postnatal Care - {self.mother.name} on {self.visit_date}'
