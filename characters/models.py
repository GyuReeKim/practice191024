from django.db import models
from django.conf import settings

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_characters")

class Character2(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    description = models.TextField()
    description2 = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_characters2")