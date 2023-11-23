from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import User,Employee,Employer,Custom_admin
admin.site.register(Custom_admin)
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Employer)
