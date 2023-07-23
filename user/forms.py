from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from .models import UserInbox
from ckeditor.fields import RichTextFormField

#User
class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    password1 = forms.CharField(label='Password:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation:', widget=forms.PasswordInput)
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        #help_texts = {k:"" for k in fields}

class UpdateUserForm(UserChangeForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = None
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar']
        #help_texts = {k:"" for k in fields}
    
class FindUserForm(forms.Form):
    username = forms.CharField(max_length=20, required=False)
    
#Inbox
class CreateInboxForm(forms.ModelForm):
    to_user = ModelChoiceField(queryset=User.objects.all(), label="To user")
    #to_user = User.objects.all()
    #options = [(f"{userItem.id}", f"{userItem.last_name}, {userItem.first_name} - username(id): {userItem.username}({userItem.id})") for userItem in User.objects.all()]
    #to_user = ModelChoiceField(queryset=options, label="To user")
    # def __init__(self, *args, **kwargs):
    #     super(CreateInboxForm, self).__init__(*args, **kwargs)
    #     to_user = User.objects.all()
    #     options = [(f"{userItem.id}", f"{userItem.last_name}, {userItem.first_name} - username(id): {userItem.username}({userItem.id})") for userItem in to_user]
    #     self.fields['to_user'] = forms.ChoiceField(choices=options)

    def get_user_label(self, user):
        return f"{user.last_name}, {user.first_name} - username(id): {user.username}({user.id})"
    
    def __init__(self, *args, **kwargs):
        super(CreateInboxForm, self).__init__(*args, **kwargs)
        self.fields['to_user'].label_from_instance = self.get_user_label
        
    class Meta:
        model = UserInbox
        fields = ['to_user', 'msg']
        
# class CreateInboxForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super(CreateInboxForm, self).__init__(*args, **kwargs)
#         to_user = User.objects.all()
#         options = [(f"{userItem.id}", f"{userItem.last_name}, {userItem.first_name} - username(id): {userItem.username}({userItem.id})") for userItem in to_user]
#         self.fields['To_user'] = forms.ChoiceField(choices=options)
#     message = RichTextFormField(required=False)
    
#     class Meta:
#         model = User
#         fields = ['to_user','message']

class FindInboxForm(forms.Form):
    msg = forms.CharField(label='Message:', max_length=20, required=False)