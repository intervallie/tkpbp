from django.db import models
from accounts.models import Account

# Create your models here.
class Consultation(models.Model):
    full_name = models.CharField(max_length=50)
    npm = models.PositiveBigIntegerField()
    date = models.DateField()
    email= models.CharField(max_length=50)

    
    selected_counselor = models.ForeignKey(Account, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.full_name
