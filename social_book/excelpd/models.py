from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=50, null=False)

class ExcelFile(models.Model):
    file = models.FileField(upload_to='excel')