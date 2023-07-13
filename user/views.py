from django.shortcuts import render, redirect
#from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
#from user.forms import CreateUserForm, UpdateUserForm, FindUserForm
#from user.models import User

#from django.views.generic.edit import UpdateView #, DeleteView, CreateView
#from django.views.generic.detail import DetailView

#from django.urls import reverse_lazy

# Create your views here.

def loginUser(request):
    
    if request.mothed == 'POST':
        formUser = AuthenticationForm(request, data=request.POST)
        if formUser.is_valid():
            fieldUser = formUser.cleaned_data['username']
            fieldPass = formUser.cleaned_data['password']
            
            user = authenticate(username=fieldUser, password=fieldPass)
            
            login(request, user)
            
            return redirect('initial:initial')
        else:
            return render(request, 'user/login_user.html', {'formUser':formUser})
    
    formUser = AuthenticationForm()
    return render(request, 'user/login_user.html', {'formUser':formUser})