from django.contrib import admin
from .models import Sensor
from .models import SensorData

admin.site.register(Sensor)
admin.site.register(SensorData)
