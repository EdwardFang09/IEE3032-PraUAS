from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class Sistem1(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class Sistem2(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class Sistem3(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class SensorData(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class Aktuator_1(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class Aktuator_2(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class Aktuator_3(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class AktuatorFinal(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)