from django.db import models

# Create your models here.
class suggestion(models.Model):
    Saran = models.TextField(max_length=200)