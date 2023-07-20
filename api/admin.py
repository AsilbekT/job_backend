from django.contrib import admin
from .models import Job, Company, Catagory, Application

# Register your models here.
admin.site.register(Job)
admin.site.register(Company)
admin.site.register(Catagory)
admin.site.register(Application)