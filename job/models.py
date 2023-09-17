from django.db import models
from django.contrib.auth.models import User

# Create your models here
class studentuser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    image = models.FileField(null = True)

    def __str__(self):
        return  self.user.username


class Recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    image = models.FileField(null = True)
    company = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return  self.user.username
    

class Contact(models.Model):
    S_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=  100)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=15)
    desc = models.TextField(max_length=500)
    timestemp = models.DateField(auto_now_add=True,blank=True)

    def __str__(self) :
        return self.name
    

class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    start_time= models.DateField(null=True)
    last_time = models.DateField(null=True)
    title = models.CharField(max_length=20)
    salary = models.FloatField(max_length=100)
    desc = models.CharField(max_length=200)
    experience = models.CharField(max_length=50)
    image = models.FileField(null = True)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    creationdate = models.DateField()#when the user post

    def __str__(self):
        return  self.title
    

class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    student= models.ForeignKey(studentuser, on_delete=models.CASCADE)
    resume = models.FileField(null=True)
    applydate = models.DateField()
    

    def __str__(self):
        return  self.student.user.username
