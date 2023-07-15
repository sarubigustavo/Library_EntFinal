from django.shortcuts import render, redirect
#from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login
from user.forms import CreateUserForm, UpdateUserForm #, FindUserForm
from user.models import UserExtra

#from django.views.generic.edit import UpdateView #, DeleteView, CreateView
#from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        formUser = AuthenticationForm(request, data=request.POST)
        if formUser.is_valid():
            fieldUser = formUser.cleaned_data['username']
            fieldPass = formUser.cleaned_data['password']
            user = authenticate(username=fieldUser, password=fieldPass)
            login(request, user)
            UserExtra.objects.get_or_create(user=user)
            return redirect('initial:initial')
        else:
            return render(request, 'user/login_user.html', {'formUser':formUser})
    formUser = AuthenticationForm()
    return render(request, 'user/login_user.html', {'formUser':formUser})

def signupUser(request):
    if request.method == 'POST':
        #formUser = UserCreationForm(request.POST)
        formUser = CreateUserForm(request.POST)
        if formUser.is_valid():
            formUser.save()
            return redirect('user:user_login') 
        else:
            return render(request, 'user/signup_user.html', {'formUser':formUser})
    #formUser = UserCreationForm()
    formUser = CreateUserForm()
    return render(request, 'user/signup_user.html', {'formUser':formUser})

@login_required
def updateUser(request):
    userextra_data = request.user.userextra
    #print("2-userextra_data.avatar->", userextra_data.avatar)
    #print("2-userextra_data.user->", userextra_data.user)
    if request.method == 'POST':
        formUser = UpdateUserForm(request.POST, request.FILES,  instance=request.user)
        if formUser.is_valid():
            #avatar
            fieldAvatar = formUser.cleaned_data.get('avatar')
            #print("1-fieldAvatar->", fieldAvatar)
            if fieldAvatar:
                userextra_data.avatar = fieldAvatar
                userextra_data.save()            
            formUser.save()
            return redirect('initial:initial') 
    else:
        formUser = UpdateUserForm(initial={'avatar': userextra_data.avatar}, instance=request.user)
        #formUser = UpdateUserForm(instance=request.user)
    return render(request, 'user/update_user.html', {'formUser':formUser})

class PasswordUser(LoginRequiredMixin, PasswordChangeView):
    #model = User
    #fields = []
    template_name = 'user/password_user.html'
    #context_object_name = 'book'
    success_url = reverse_lazy('user:user_update')