from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView

app_name = 'user'

urlpatterns = [
    path('users/login', views.loginUser, name='user_login'),
    path('users/signup', views.signupUser, name='user_signup'),
    path('users/logout', LogoutView.as_view(template_name='user/logout_user.html'), name='user_logout'),
    path('users/update', views.updateUser, name='user_update'), #Ver template
    path('users/password', views.PasswordUser.as_view(), name='user_password'), #Ver template
]