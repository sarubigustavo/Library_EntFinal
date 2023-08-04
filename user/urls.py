from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView

app_name = 'user'

urlpatterns = [
    #Users
    path('users/login', views.loginUser, name='user_login'),
    path('users/signup', views.signupUser, name='user_signup'),
    path('users/logout', LogoutView.as_view(template_name='user/logout_user.html'), name='user_logout'),
    path('users/detail/<int:pk>/', views.DetailUser.as_view(), name='user_detail'), #CBV
    path('users/update', views.updateUser, name='user_update'), #Ver template
    path('users/password', views.PasswordUser.as_view(), name='user_password'), #Ver template
    #Inbox
    path('inbox/list', views.listInbox, name='inbox_list'),
    path('inbox/create', views.createInbox, name='inbox_create'),
    path('inbox/delete/<int:inbox_id>/', views.deleteInbox, name='inbox_delete'),
    path('inbox/detail/<int:pk>/', views.DetailInbox.as_view(), name='inbox_detail'), #CBV
]