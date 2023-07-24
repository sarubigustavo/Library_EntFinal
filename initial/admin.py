from django.contrib import admin
from initial.models import Book, Client
from user.models import UserInbox

# Register your models here.
admin.site.register(Book)
admin.site.register(Client)
admin.site.register(UserInbox)
#admin.site.register(UserExtra)