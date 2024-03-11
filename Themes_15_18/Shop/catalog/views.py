from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic.edit import  FormView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')
    

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)
    

def logout_view(request):
    logout(request)
    return redirect('index')


def index(request):
     context = {
         'title': 'Главная страница сайта' 
         }
     return render(request, 'index.html', context)


def manufacturer_list(request):
    return render(request, 'manufacturer_list.html')


def display_manufacturers(request):
    manufacturers = Manufacturer.objects.all()

    context = {
        'manufacturers': manufacturers,
        'header': 'Manufacturer' 
    }   

    return render(request, 'manufacturer_list.html', context)


def add_manufacturer(request):
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('manufacturer_list')
    else:
        form = ManufacturerForm()
        context = {
            'form': form,
            'header': 'Manufacturer'
        }   
        return render(request, 'add_manufacturer.html', context)
    

def product_list(request):
    return render(request, 'product_list.html')


def display_products(request):
    items = Product.objects.all()
    context = {
        'items': items,
        'header': 'Product'
    }     

    return render(request, 'product_list.html', context)


def add_product(request, header="Добавление товара"):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()           
            return redirect('product_list')
    else:
        form = ProductForm()

        context = {
            'form': form,            
            'header': header,            
        }   
    
    return render(request, 'add_product.html', context)
    