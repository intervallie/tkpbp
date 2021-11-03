from django.db import models
from django.utils.text import slugify
# Create your models here.
class Article(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    desc = models.CharField(max_length = 300)
    article = models.TextField()
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
