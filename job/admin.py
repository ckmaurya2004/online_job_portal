from django.contrib import admin
from  . models import studentuser,Contact,Recruiter,Job,Apply

# Register your models here.
admin.site.register((studentuser,Contact,Recruiter,Job,Apply))
