from django.db import models

# Create your models here.
class Studentreg(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    contact=models.IntegerField()
    std_email=models.CharField(max_length=20)

class Studentlogin(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    std_id=models.ForeignKey(Studentreg,on_delete=models.CASCADE)

class Employee(models.Model):
    name=models.CharField(max_length=20)
    contact=models.IntegerField()
    place=models.CharField(max_length=25)
    result=models.FileField(upload_to='Results/')

class Apidemo(models.Model):
    name=models.CharField(max_length=20)
    contact=models.IntegerField()
    place=models.CharField(max_length=25)
    result=models.FileField(upload_to='Results/')