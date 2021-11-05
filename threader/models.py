from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class Thread(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images', blank=True, null=True)
    
    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": 0
        }