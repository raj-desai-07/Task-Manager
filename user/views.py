from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from task.models import Task

def userRegister(request):
    if request.method == "POST":
        name = request.POST.get("rg-name")
        email = request.POST.get("rg-email")
        password = request.POST.get("rg-password")

        User.objects.create(name=name, email=email, password=password)

        messages.success(request, "Register Successfully..! Try to Login")
        return redirect("/login/")
    else:
        return redirect("/login/")
    
def userLogin(request):
    if request.method == "POST":
        email = request.POST.get("lg-email")
        password = request.POST.get("lg-password")

        if User.objects.filter(email=email, password=password).exists():
            loggedUser = User.objects.filter(email=email, password=password).first()
            request.session['name'] = loggedUser.name
            request.session['user'] = loggedUser.email
            request.session['joined'] = loggedUser.joined.strftime('%Y-%m-%d')
            return redirect("/")
        else:
            messages.error(request, "User Does't Exist..! Try Again")
            return redirect("/login/")
    else:
        return redirect("/login/")
    
def logout(request):
    del request.session["name"]
    del request.session["user"]
    del request.session["joined"]
    return redirect("/login/")

def deleteAccount(request):
    if request.method == "POST":
        User.objects.filter(email=request.session['user']).first().delete()
        del request.session["name"]
        del request.session["user"]
        del request.session["joined"]
        messages.error(request, "Account Deleted..!")
        return redirect("/login/")
    else:
        return redirect("/")