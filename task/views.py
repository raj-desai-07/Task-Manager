from django.shortcuts import render, redirect
from .models import Task
from user.models import User
from django.contrib import messages

def addTask(request):
    if request.method == "POST":
        name = request.POST.get("add-name")
        subject = request.POST.get("add-subject")
        dis = request.POST.get("add-dis")
        date = request.POST.get("add-date")
        uid = User.objects.filter(email=request.session["user"]).first()

        Task.objects.create(name=name, subject=subject, discription=dis, date=date, uid=uid)

        return redirect("/")

    else:
        return redirect("/")
    
def updateTask(request):
    if request.method == "POST":
        upId = request.POST.get("up-id")
        name = request.POST.get("up-name")
        subject = request.POST.get("up-subject")
        dis = request.POST.get("up-dis")
        date = request.POST.get("up-date")
        status = request.POST.get("up-status")

        task = Task.objects.get(id=upId)

        task.name = name
        task.subject = subject
        task.discription = dis
        task.date = date
        task.status = status

        task.save()
        return redirect("/")
    else:
        return redirect("/")
    
def deleteTask(request):
    if request.method == "POST":
        taskId = request.POST.get("del-id")
        selectedTask = Task.objects.get(id=taskId)
        selectedTask.delete()

        return redirect("/")
    else:
        return render("/")