from django.contrib import admin
from initial.models import User, Book, Client

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Client)