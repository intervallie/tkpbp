from django.db import models

# Create your models here.
class Consultation(models.Model):
    full_name = models.CharField(max_length=50)
    npm = models.PositiveBigIntegerField()
    date = models.DateField()
    email= models.CharField(max_length=50)

    