from django.urls import path
from initial import views

app_name = 'initial'

urlpatterns = [
    path('', views.initial, name='initial'),
    path('about', views.about, name='about'),
    #Book
    path('books/create', views.createBook, name='book_create'),
    path('books/list', views.listBook, name='book_list'),
    path('books/delete/<int:book_id>/', views.deleteBook, name='book_delete'),
    #Client
    path('clients/create', views.createClient, name='client_create'),
    path('clients/list', views.listClient, name='client_list'),
    path('clients/delete/<int:client_id>/', views.deleteClient, name='client_delete'),
    #User
    path('users/create', views.createUser, name='user_create'),
    path('users/list', views.listUser, name='user_list'),
    path('users/delete/<int:user_id>/', views.deleteUser, name='user_delete'),
]