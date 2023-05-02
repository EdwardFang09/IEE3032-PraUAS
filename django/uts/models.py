from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class SensorData(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
