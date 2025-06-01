from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100, unique=True)
    # slug =models.SlugField(max_length=100)
    
    reg_no = models.CharField(unique=True,max_length=50)

    def __str__(self):
        return f"{self.first_name}"
    

class Admin(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    

class Maintenance(models.Model):
    STATUS_CHOICES = {
        "PENDING":"PENDING",
        "IN PROGRESS":"IN PROGRESS",
        "COMPLETE":"COMPLETE"
    }
    sender = models.ForeignKey(Student, on_delete=models.CASCADE)
    item = models.CharField(max_length=25)
    detail = models.TextField(max_length=500)
    status = models.CharField(choices=STATUS_CHOICES, default="PENDING")

    def __str__(self):
        return self.item
    

class Suggestion(models.Model):
    MY_CHOICES = {
        "PENDING":"PENDING",
        "DELIVERED":"DELIVERED"
    }

    sender = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    status = models.TextField(choices=MY_CHOICES, default="PENDING")

    def __str__(self):
        return f"{self.sender}"