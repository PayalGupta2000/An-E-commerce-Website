from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    products=Product.objects.all().filter(is_available=True)
    
    context={
        'products':products,
        
    }
    return render(request,"home.html",context)

def store(request,category_slug=None):
    categories=None
    products=None
    if category_slug != None:
        categories=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(category=categories,is_available=True)
        product_count=products.count()
    else:
        products=Product.objects.all().filter(is_available=True)
        product_count=products.count()
        context={
            'products':products,
            'product_count':product_count
        }
        return render(request,"store.html",context)

def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)