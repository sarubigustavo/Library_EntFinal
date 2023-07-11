from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    edition = models.DateField(null=True)
    #descripcion = ..RichField
    
class Client(models.Model):
    dni = models.IntegerField()
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20, null=True)
    #observaciones = ..RichField
    
class User(models.Model):
    fullname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    userpass = models.CharField(max_length=20)
    