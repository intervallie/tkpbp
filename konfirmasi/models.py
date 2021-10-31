from django.db import models

# Create your models here.
class Consultation(models.Model):
    full_name = models.CharField(max_length=150)
    npm = models.CharField(max_length=50)
    date = models.DateField()
    email = models.CharField(max_length=50)