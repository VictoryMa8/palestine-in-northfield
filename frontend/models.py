from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class Post(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(blank=True, null=True, max_length=1000)
    image = models.ImageField(upload_to='frontend/static/uploads/')

    def __str__(self):
        return self.title