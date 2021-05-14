from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.
from .models import *
from .forms import CreateUserForm, CreateProductFrom

def index(request):
    #return HttpResponse("<h1>Welcome</h1>")
    products=Product.objects.all()
    print(products)
    context={"products":products}
    return render(request, "index.html",context)

@login_required(login_url='signin')
def indexlogin(request):
    products=Product.objects.all()
    print(products)
    context={"products":products}
    return render(request, "indexlogin.html",context)

def logoutUser(request):
    logout(request)
    return redirect('signin')

def signin(request):
    if request.user.is_authenticated:
        return redirect('indexlogin')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('indexlogin')
            else:
                messages.info(request, "Username OR Password is incorrect")
    context = {}
    return render(request, 'signin.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('indexlogin')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created successfully for " + user)
                return redirect('signin')
    context = {'form': form}
    return render(request, 'signup.html', context)

@login_required(login_url='signin')
def postad(request):
    form = CreateProductFrom()
    if(request.method == 'POST'):
        form = CreateProductFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('allads')
    context = {'form': form}
    return render(request, 'post-ad.html', context)

#def allads(request):
#    return render(request, 'all-classifieds.html')

class AllAdsView(ListView):
    model = Product
    template_name = 'newclassifields.html'

class ProductView(DetailView):
    model = Product
    template_name = 'single.html'

def CategoryView(request, cats):
    category_posts = Product.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats, 'category_posts': category_posts})
