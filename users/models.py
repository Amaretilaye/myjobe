from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_custom_admin= models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=20)
    username=models.CharField(max_length=20)
    password1=models.CharField(max_length=20)
    password2=models.CharField(max_length=20)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password1=models.CharField(max_length=20)
    password2=models.CharField(max_length=20)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
   
class Custom_admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return str(self.user)