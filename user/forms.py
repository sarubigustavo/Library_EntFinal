from django import forms
from django.contrib.auth.forms import UserCreationForm   
from django.contrib.auth.models import User

#User
class BaseUserForm(UserCreationForm):
    fullname = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(label='Password:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation:', widget=forms.PasswordInput)
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['fullname', 'email', 'username', 'password1', 'password2']
        #help_texts = {k:"" for k in fields}
    
class CreateUserForm(BaseUserForm):
    ...
    
class UpdateUserForm(BaseUserForm):
    ...
    
class FindUserForm(forms.Form):
    username = forms.CharField(max_length=20, required=False)