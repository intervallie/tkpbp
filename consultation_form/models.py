from django.db import models
from accounts.models import Account

# Create your models here.
class Consultation(models.Model):
    full_name = models.CharField(max_length=50)
    npm = models.PositiveBigIntegerField()
    date = models.DateField()
    email= models.CharField(max_length=50)
<<<<<<< HEAD

    
=======
    selected_counselor = models.ForeignKey(Account, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.full_name
>>>>>>> ef4dac5acf525658730f8ca44cab4c11378dada2
