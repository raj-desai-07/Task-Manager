from django.db import models
from datetime import datetime

today = datetime.now().date()

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=777, null=False)
    password = models.CharField(max_length=25)
    joined = models.DateField(default=today)