from django import forms

#Book
class CreateBookForm(forms.Form):
    isbn = forms.IntegerField()
    title = forms.CharField(max_length=20)
    author = forms.CharField(max_length=20)
    #edition = forms.DateField(required=False)
    edition = forms.DateField(required=False, widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker', 'placeholder': 'DD/MM/YYYY'}), input_formats=('%d/%m/%Y', ))

class FindBookForm(forms.Form):
    title = forms.CharField(max_length=20, required=False)
    
#Client
class CreateClientForm(forms.Form):
    dni = forms.IntegerField()
    lastname = forms.CharField(max_length=20)
    firstname = forms.CharField(max_length=20, required=False)

class FindClientForm(forms.Form):
    lastname = forms.CharField(max_length=20, required=False)
    
#User
class CreateUserForm(forms.Form):
    fullname = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    userpass = forms.CharField(max_length=20)

class FindUserForm(forms.Form):
    username = forms.CharField(max_length=20, required=False)