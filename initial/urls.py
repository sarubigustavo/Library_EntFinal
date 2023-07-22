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
    path('books/update/<int:book_id>/', views.updateBook, name='book_update'),
    path('books/detail/<int:pk>/', views.DetailBook.as_view(), name='book_detail'), #CBV
    
    #Client
    path('clients/create', views.createClient, name='client_create'),
    path('clients/list', views.listClient, name='client_list'),
    path('clients/delete/<int:client_id>/', views.deleteClient, name='client_delete'),
    path('clients/update/<int:pk>/', views.UpdateClient.as_view(), name='client_update'), #CBV
    path('clients/detail/<int:pk>/', views.DetailClient.as_view(), name='client_detail'), #CBV
    
    #User
    path('users/create', views.createUser, name='user_create'),
    #path('users/list', views.listUser, name='user_list'),
    path('users/delete/<int:user_id>/', views.deleteUser, name='user_delete'),
    #path('users/update/<int:pk>/', views.UpdateUser.as_view(), name='user_update'), #CBV
    path('users/detail/<int:pk>/', views.DetailUser.as_view(), name='user_detail'), #CBV
]