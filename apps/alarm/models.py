from django.db import models
from django.utils import timezone


class Patient(models.Model):

    name = models.CharField(
        max_length=50
    )

    disease = models.CharField(
        max_length=50
    )

    medicament = models.CharField(
        max_length=50
    )

    created_date = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.name


class Alarm(models.Model):

    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE
    )

    notification = models.DateTimeField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_date = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return '{} {}' .format(self.patient, self.notification)


class CareNetwork(models.Model):

    careman = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    created_date = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return '{} {}'.format(self.careman, self.patient)
