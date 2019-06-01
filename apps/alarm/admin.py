from django.contrib import admin
from .models import Patient, Alarm, CareNetwork

admin.site.register(Patient)
admin.site.register(Alarm)
admin.site.register(CareNetwork)
