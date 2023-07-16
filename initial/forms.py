from django import forms

#Book
class BaseBookForm(forms.Form):
    isbn = forms.IntegerField()
    title = forms.CharField(max_length=20)
    author = forms.CharField(max_length=20)
    edition = forms.DateField(required=False, widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker', 'placeholder': 'DD/MM/YYYY'}), input_formats=('%d/%m/%Y', ))
    bookcover = forms.ImageField(required=False)
    description = forms.CharField(max_length=100, required=False)
    
class CreateBookForm(BaseBookForm):
    ...
    
class UpdateBookForm(BaseBookForm):
    ...
    
class FindBookForm(forms.Form):
    title = forms.CharField(max_length=20, required=False)
    
    
#Client
class BaseClientForm(forms.Form):
    dni = forms.IntegerField()
    lastname = forms.CharField(max_length=20)
    firstname = forms.CharField(max_length=20, required=False)
    email = forms.CharField(max_length=20, required=False)
    comments = forms.CharField(max_length=100, required=False)
    
class CreateClientForm(BaseClientForm):
    ...

class UpdateClientForm(BaseClientForm):
    ...

class FindClientForm(forms.Form):
    lastname = forms.CharField(max_length=20, required=False)
    
#User
class BaseUserForm(forms.Form):
    fullname = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    userpass = forms.CharField(max_length=20)
    
class CreateUserForm(BaseUserForm):
    ...
    
class UpdateUserForm(BaseUserForm):
    ...
    
class FindUserForm(forms.Form):
    username = forms.CharField(max_length=20, required=False)