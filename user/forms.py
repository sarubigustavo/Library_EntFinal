from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from .models import UserInbox, UserExtra
from ckeditor.fields import RichTextFormField

#User
class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    password1 = forms.CharField(label='Password:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation:', widget=forms.PasswordInput)
    email = forms.EmailField()
    shift = forms.ChoiceField(choices=UserExtra.Shifts)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'shift', 'username', 'password1', 'password2']
        #help_texts = {k:"" for k in fields}

class UpdateUserForm(UserChangeForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    shift = forms.ChoiceField(choices=UserExtra.Shifts)
    password = None
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'shift', 'avatar']
        #help_texts = {k:"" for k in fields}
    
class FindUserForm(forms.Form):
    username = forms.CharField(max_length=20, required=False)
    
#Inbox
class CreateInboxForm(forms.ModelForm):
    to_user = ModelChoiceField(queryset=User.objects.all(), label="To user")

    def get_user_label(self, user):
        return f"{user.last_name}, {user.first_name} - username(id): {user.username}({user.id})"
    
    def __init__(self, *args, **kwargs):
        super(CreateInboxForm, self).__init__(*args, **kwargs)
        self.fields['to_user'].label_from_instance = self.get_user_label
        
    class Meta:
        model = UserInbox
        fields = ['to_user', 'msg']
        
class FindInboxForm(forms.Form):
    msg = forms.CharField(label='Message:', max_length=20, required=False)