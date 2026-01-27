from django.shortcuts import render, redirect
from task.models import Task
from user.models import User

def redirectHome(request):
    userEmail = request.session.get('user')
    if userEmail:
        # userEmail = request.session['user']
        usr = User.objects.get(email=userEmail)
        allTasks = Task.objects.filter(uid=usr).order_by("-id")
        print(request.session.items())
        return render(request, "index.html", {"tasks": allTasks})
    else:
        return redirect("/login/")

def redirectChangePassword(request):
    return render(request, "change-password.html")

def redirectDeleteAccount(request):
    return render(request, "confirm-delete.html")

def redirectLogin(request):
    return render(request, "login.html")

def redirect404(request):
    return render(request, "404.html")