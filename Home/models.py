from django.db import models

# Create your models here.
class TblData(models.Model):
   temperature = models.CharField(max_length=20)
   humidity = models.CharField(max_length=20)
   Datefild= models.DateField(null=True)
   timefild=models.CharField(max_length=20,null=True)


   def __str__(self):
      return f"{self.temperature} ({self.humidity})"