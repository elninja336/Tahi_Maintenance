from django.db import models

# Create your models here.

class Student(models.Model):
    # first_name = models.CharField(max_length=25)
    # middle_name = models.CharField(max_length=25)
    # last_name = models.CharField(max_length=25)
    # slug =models.SlugField(max_length=100)

    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    student_id = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.fullname}"
    

class Admin(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.user_name}"
    

class Maintenance(models.Model):
    STATUS_CHOICES = {
        "PENDING":"PENDING",
        "IN PROGRESS":"IN PROGRESS",
        "RESOLVED":"RESOLVED"
    }
    Student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    status = models.CharField(choices=STATUS_CHOICES, default="PENDING")
    image = models.ImageField(blank=True, null=True)
    reply = models.CharField(max_length=500, null=True, blank=True,default=None)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    

class Suggestion(models.Model):
    MY_CHOICES = {
        "PENDING":"PENDING",
        "IN PROGRESS":"IN PROGRESS",
        "RESOLVED":"RESOLVED"
    }

    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    status = models.TextField(choices=MY_CHOICES, default="PENDING")
    image = models.ImageField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message}"