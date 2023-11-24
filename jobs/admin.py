from django.contrib import admin
from.models import Categories,EmployeeProfile,ProfilePic,EmployerProfile,Job,Applicant
# Register your models here.
admin.site.register(Categories)

admin.site.register(EmployeeProfile)
admin.site.register(ProfilePic)
admin.site.register(EmployerProfile)
admin.site.register(Job)
admin.site.register(Applicant)