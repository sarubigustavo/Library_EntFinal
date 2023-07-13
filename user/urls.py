from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('users/login', views.loginUser, name='user_login'),
]