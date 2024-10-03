from django.db import models

# Create your models here.
class Student(models.Model):
    ID = models.AutoField(primary_key=True)
    Name  = models.CharField(max_length=100)
    Age = models.IntegerField()
    E_mail = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


