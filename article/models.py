from django.db import models
from django.utils.text import slugify
# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 300)
    date = models.DateTimeField(auto_now=True)
    article = models.TextField()
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title