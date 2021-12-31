from django.db import models

# Create your models here.
NOMINAL_CHOICES = [
    ('Rp50.000', 'Rp50.000'),
    ('Rp100.000', 'Rp100.000'),
    ('Rp250.000', 'Rp250.000'),
    ('Rp500.000', 'Rp500.000'),
    ('Rp1.000.000', 'Rp1.000.000'),
]

class Donasi(models.Model):
    nama = models.CharField(max_length=100)
    nominal = models.CharField(choices=NOMINAL_CHOICES, default='Rp50.000', max_length=12)
    bukti_Transfer = models.TextField()

    def __str__(self):
        return self.nama