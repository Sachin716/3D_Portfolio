from django.shortcuts import render

def Home(request):
    return render(request,"User/index.html")

def login_page(request):
    return render(request,"Adm/login.html")

def admin_page(request):
    return render(request,"Adm/edit_category.html")