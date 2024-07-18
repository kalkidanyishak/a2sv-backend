from django.db import models

class Surveyor(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    assigned_region = models.CharField(max_length=100)

    def __str__(self):
        return self.name
