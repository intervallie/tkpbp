from django.db import models
from consultation_form.models import Consultation

# Create your models here.
class Konsultasi(models.Model):
    full_name = models.CharField(max_length=150)
    npm = models.CharField(max_length=50)
    date = models.DateField()
    email = models.CharField(max_length=50)

    selected_accept = models.ForeignKey(Consultation, on_delete=models.CASCADE, default=None)