from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Student(models.Model):
    rn = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    marks = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)