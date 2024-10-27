from django.db import models

# Create your models here.
class TblData(models.Model):
   temperature = models.CharField(max_length=20)
   humidity = models.CharField(max_length=20)