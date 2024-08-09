from django.shortcuts import render , HttpResponse
from .models import *

def Home(request):
    return render(request,"User/index.html")

def login_page(request):
    return render(request,"Adm/login.html")

def admin_page(request):
    models = category.objects.all()
    return render(request,"Adm/edit_category.html" , {
        'models':models
    })

def Admin_Multiple_items(request , category_item):
    return render(request,"Adm/edit_Multiple_Projects.html")

def Admin_Single_item(request,id):
    return render(request,"Adm/edit_Single_project.html")

def register_user(request):
    return render(request,"Adm/register.html")