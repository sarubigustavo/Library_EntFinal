from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar_folder', null=True, blank=True)