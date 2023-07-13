from django.shortcuts import render, redirect
#from django.http import HttpResponse

from initial.forms import CreateBookForm, UpdateBookForm, FindBookForm, CreateClientForm, UpdateClientForm, FindClientForm, CreateUserForm, UpdateUserForm, FindUserForm
from initial.models import Book, Client, User

from django.views.generic.edit import UpdateView #, DeleteView, CreateView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

# Create your views here.

def initial(request):
    return render(request, 'initial/initial.html')

def about(request):
    return render(request, 'initial/about.html')

#Book
def createBook(request):
    #msgLabel = ''
    if request.method == 'POST':
        formBook = CreateBookForm(request.POST)
        if formBook.is_valid():
            infoBook = formBook.cleaned_data
            book = Book(isbn=infoBook['isbn'], title=infoBook['title'], author=infoBook['author'], edition=infoBook['edition'])
            book.save()
            #msgLabel =  f'Book "{book.title}" has been created.'
            return redirect('initial:book_list')
        else:
            return render(request, 'initial/create_book.html', {'formBook': formBook})
        
    formBook = CreateBookForm()
    return render(request, 'initial/create_book.html', {'formBook': formBook})
    #return render(request, 'initial/create_book.html', {'formBook': formBook, 'msgLabel': msgLabel})
    
def listBook(request):
    formBook = FindBookForm(request.GET)
    if formBook.is_valid():
        titleBook = formBook.cleaned_data['title']
        listBook = Book.objects.filter(title__icontains=titleBook)

    formBook = FindBookForm()
    return render(request, 'initial/list_book.html', {'formBook': formBook, 'listBook': listBook})
    
def deleteBook(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('initial:book_list')
    
def updateBook(request, book_id):
    book_to_update = Book.objects.get(id=book_id)
    
    if request.method == 'POST':
        formBook = UpdateBookForm(request.POST)
        if formBook.is_valid():
            infoBook = formBook.cleaned_data
            book_to_update.isbn = infoBook['isbn']
            book_to_update.title = infoBook['title']
            book_to_update.author=infoBook['author']
            book_to_update.edition=infoBook['edition']
            book_to_update.save()
            return redirect('initial:book_list')
        else:
            return render(request, 'initial/update_book.html', {'formBook': formBook})
        
    formBook = UpdateBookForm(initial={'isbn':book_to_update.isbn, 'title':book_to_update.title, 'author':book_to_update.author, 'edition':book_to_update.edition})
    return render(request, 'initial/update_book.html', {'formBook': formBook})

class DetailBook(DetailView):
    model = Book
    #fields = []
    template_name = "initial/CBV/detail_book.html"
    #context_object_name = 'book'
    #success_url = reverse_lazy('initial:book_list')

#Client
def createClient(request):
    #msgLabel = ''
    if request.method == 'POST':
        formClient = CreateClientForm(request.POST)
        if formClient.is_valid():
            infoClient = formClient.cleaned_data
            client = Client(dni=infoClient['dni'], lastname=infoClient['lastname'], firstname=infoClient['firstname'])
            client.save()
            #msgLabel =  f'Book "{book.title}" has been created.'
            return redirect('initial:client_list')
        else:
            return render(request, 'initial/create_client.html', {'formClient': formClient})
        
    formClient = CreateClientForm()
    return render(request, 'initial/create_client.html', {'formClient': formClient})
    #return render(request, 'initial/create_client.html', {'formClient': formClient, 'msgLabel': msgLabel})
    
def listClient(request):
    formClient = FindClientForm(request.GET)
    if formClient.is_valid():
        lastnameClient = formClient.cleaned_data['lastname']
        listClient = Client.objects.filter(lastname__icontains=lastnameClient)

    formClient = FindClientForm()
    return render(request, 'initial/list_client.html', {'formClient': formClient, 'listClient': listClient})

def deleteClient(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    return redirect('initial:client_list')

class UpdateClient(UpdateView):
    model = Client
    fields = ['dni','lastname','firstname']
    template_name = "initial/CBV/update_client.html"
    #context_object_name = 'client'
    success_url = reverse_lazy('initial:client_list')
    
class DetailClient(DetailView):
    model = Client
    #fields = []
    template_name = "initial/CBV/detail_client.html"
    #context_object_name = 'client'
    #success_url = reverse_lazy('initial:client_list')

#User
def createUser(request):
    #msgLabel = ''
    if request.method == 'POST':
        formUser = CreateUserForm(request.POST)
        if formUser.is_valid():
            infoUser = formUser.cleaned_data
            user = User(fullname=infoUser['fullname'], username=infoUser['username'], userpass=infoUser['userpass'])
            user.save()
            #msgLabel =  f'Book "{book.title}" has been created.'
            return redirect('initial:user_list')
        else:
            return render(request, 'initial/create_user.html', {'formUser': formUser})
        
    formUser = CreateUserForm()
    return render(request, 'initial/create_user.html', {'formUser': formUser})
    #return render(request, 'initial/create_user.html', {'formUser': formUser, 'msgLabel': msgLabel})
    
def listUser(request):
    formUser = FindUserForm(request.GET)
    if formUser.is_valid():
        usernameUser = formUser.cleaned_data['username']
        listUser = User.objects.filter(username__icontains=usernameUser)

    formUser = FindUserForm()
    return render(request, 'initial/list_user.html', {'formUser': formUser, 'listUser': listUser})

def deleteUser(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('initial:user_list')

class UpdateUser(UpdateView):
    model = User
    fields = ['fullname','username','userpass']
    template_name = "initial/CBV/update_user.html"
    #context_object_name = 'user'
    success_url = reverse_lazy('initial:user_list')
    
class DetailUser(DetailView):
    model = User
    #fields = []
    template_name = "initial/CBV/detail_user.html"
    #context_object_name = 'user'
    #success_url = reverse_lazy('initial:client_list')
