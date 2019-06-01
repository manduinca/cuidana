from django.db import models
from django.utils import timezone


class Patient(models.Model):
    name = models.CharField(max_length=50)
    disease = models.CharField(max_length=50)
    medicament = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)


class Alarm(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    emision_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)


class CareNetwork(models.Model):
    careman = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
