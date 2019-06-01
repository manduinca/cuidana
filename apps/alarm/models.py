from django.db import models
from django.utils import timezone


class Patient(models.Model):
    name = models.CharField(max_length=50)
    disease = models.CharField(max_length=50)
    medicament = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Alamr(models.Model):
    patient = models.ForeignKey('models.Patient', on_delete=models.CASCADE)
    emision_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(initial=True)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.emision_date


class CareNetwork(models.Model):
    careman = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    patient = models.ForeignKey('models.Patient', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.careman

