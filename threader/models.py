from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class ThreadLike(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    thread = models.ForeignKey("Thread", default=None, null=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Thread(models.Model):
    # id = models.AutoField(primary_key=True)
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=ThreadLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": 0
        }