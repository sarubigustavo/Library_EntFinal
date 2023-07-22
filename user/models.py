from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class UserExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar_folder', null=True, blank=True)
    
    def __str__(self):
        return f"user: {self.user} - avatar: {self.avatar}"

class UserInbox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = RichTextField(null=True, blank=True)
    createdbyuser = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return f"user: {self.user} - msg: {self.msg} - createdbyuser: {self.createdbyuser}"