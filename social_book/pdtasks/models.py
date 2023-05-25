from django.db import models

# Create your models here.

class NewBook(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, null=False)
    author = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=False)
    date_of_sale = models.DateField(null=False)
