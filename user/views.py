from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login
from user.forms import CreateUserForm, UpdateUserForm, CreateInboxForm, FindInboxForm
from user.models import UserExtra, UserInbox, User

from django.views.generic.detail import DetailView

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
        formUser = CreateUserForm(request.POST)
        if formUser.is_valid():
            formUser.save()
            return redirect('user:user_login') 
        else:
            return render(request, 'user/signup_user.html', {'formUser':formUser})
    formUser = CreateUserForm()
    return render(request, 'user/signup_user.html', {'formUser':formUser})

class DetailUser(LoginRequiredMixin, DetailView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'shift', 'avatar']
    template_name = "user/CBV/detail_user.html"
    #context_object_name = 'user'
    #success_url = reverse_lazy('initial:client_list')

@login_required
def updateUser(request):
    userextra_data = request.user.userextra
    if request.method == 'POST':
        formUser = UpdateUserForm(request.POST, request.FILES,  instance=request.user)
        if formUser.is_valid():
            #avatar
            fieldAvatar = formUser.cleaned_data.get('avatar')
            if fieldAvatar:
                userextra_data.avatar = fieldAvatar
            fieldShift = formUser.cleaned_data.get('shift')
            userextra_data.shift = fieldShift
            userextra_data.save()            
            formUser.save()
            return redirect('user:user_detail', request.user.id) 
    else:
        formUser = UpdateUserForm(initial={'avatar': userextra_data.avatar, 'shift': userextra_data.shift}, instance=request.user)
    return render(request, 'user/update_user.html', {'formUser':formUser})

class PasswordUser(LoginRequiredMixin, PasswordChangeView):
    #model = User
    #fields = []
    template_name = 'user/password_user.html'
    #context_object_name = 'book'
    success_url = reverse_lazy('user:user_update')
    

#User comming from Initial 
@login_required
def createInbox(request):
    #msgLabel = ''
    if request.method == 'POST':
        formMsg = CreateInboxForm(request.POST)
        if formMsg.is_valid():
            new_message = formMsg.save(commit=False)
            new_message.user = formMsg.cleaned_data['to_user']
            new_message.createdbyuser = request.user  
            new_message.save()
            #msgLabel =  f'Book "{book.title}" has been created.'
            return redirect('user:inbox_list')
        else:
            return render(request, 'user/create_msg.html', {'formMsg': formMsg})
        
    formMsg = CreateInboxForm()
    return render(request, 'user/create_msg.html', {'formMsg': formMsg})

@login_required   
def listInbox(request):
    formInbox = FindInboxForm(request.GET)
    if formInbox.is_valid():
        msgForm = formInbox.cleaned_data['msg']
        print(f"request.user.id={request.user.id}")
        listInbox = UserInbox.objects.filter(msg__icontains=msgForm, user=request.user.id) #,id=request.user.id) #.exclude(id__in=request.user.id)

    formInbox = FindInboxForm()
    return render(request, 'user/list_inbox.html', {'formInbox': formInbox, 'listInbox': listInbox})

@login_required
def deleteInbox(request, inbox_id):
    msg = UserInbox.objects.get(id=inbox_id)
    msg.delete()
    return redirect('user:inbox_list')

class DetailInbox(LoginRequiredMixin, DetailView):
    model = UserInbox
    #fields = []
    template_name = "user/CBV/detail_inbox.html"
    #context_object_name = 'user'
    #success_url = reverse_lazy('initial:client_list')
