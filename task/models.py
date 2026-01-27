from django.db import models
from user.models import User

class Task(models.Model):
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    discription = models.CharField(max_length=1000)
    date = models.DateField(null=False)
    status = models.CharField(max_length=25, default="pending")
    uid = models.ForeignKey(User, on_delete=models.CASCADE, null=False)