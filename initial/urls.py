from django.urls import path
from initial import views

app_name = 'initial'

urlpatterns = [
    path('', views.initial, name='initial'),
    path('about', views.about, name='about'),
    #Book
    path('books/create', views.createBook, name='book_create'),
    path('books/list', views.listBook, name='book_list'),
    #Client
    path('clients/create', views.createClient, name='client_create'),
    path('clients/list', views.listClient, name='client_list'),
    #User
    path('users/create', views.createUser, name='user_create'),
    path('users/list', views.listUser, name='user_list'),
]