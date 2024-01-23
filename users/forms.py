from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms 
from jobs.models import EmployeeProfile,Categories,ProfilePic,EmployerProfile,Job 
from jobs.models import*
from django.db import transaction
from .models import User,Employer,Employee
from django.urls import reverse_lazy
from jobs.forms import ApplicantForm

class EmployerSignUpForm(UserCreationForm):
    company_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('company_name', 'email', 'username', 'password1', 'password2')

    @transaction.atomic
    def save(self):
      user = super().save(commit=False)
      user.is_employer = True
      user.is_staff = True
      user.save()

      employer = Employer.objects.create(user=user)
      employer.company_name = self.cleaned_data.get('company_name')  # Fix the typo here
      employer.email = self.cleaned_data.get('email')
      employer.save()

      return user

class EmployeeSignUpForm(UserCreationForm):
    # Your form fields
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'username', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        user.save()

        employee = Employee.objects.create(user=user)
        employee.first_name = self.cleaned_data.get('first_name')
        employee.last_name = self.cleaned_data.get('last_name')
        employee.save()

        return user
class ProfilePageForm(forms.ModelForm):
    
    class Meta:
        model = EmployeeProfile
        fields = (
            'bio',
            'web_site_url',
            'instagram_url',
            'facebooke_url',
            'telegram_url',
            'email',
            'profile_pic',
            'skills',
            'education',
            'experience',
            'certifications',
            'languages',
            'linkedin_url',
            'portfolio_url',
        )
        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'web_site_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebooke_url': forms.TextInput(attrs={'class': 'form-control'}),
            'telegram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-item'}),  # Change this line
            'education': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.Textarea(attrs={'class': 'form-control'}),
            'certifications': forms.TextInput(attrs={'class': 'form-control'}),
            'languages': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
            'portfolio_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

    skills = forms.ModelMultipleChoiceField(
        queryset=Categories.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-item'}),
        required=False,
    )
class EditProfileForm(forms.ModelForm):
   
    class Meta:
        model = EmployeeProfile
        fields = (
            'bio',
            'web_site_url',
            'instagram_url',
            'facebooke_url',
            'telegram_url',
            'email',
            'profile_pic',
            'skills',
            'education',
            'experience',
            'certifications',
            'languages',
            'linkedin_url',
            'portfolio_url',
        )
        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'web_site_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebooke_url': forms.TextInput(attrs={'class': 'form-control'}),
            'telegram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-item'}),  # Change this line
            'education': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.Textarea(attrs={'class': 'form-control'}),
            'certifications': forms.TextInput(attrs={'class': 'form-control'}),
            'languages': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
            'portfolio_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

    skills = forms.ModelMultipleChoiceField(
        queryset=Categories.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-item'}),
        required=False,
    )
   
class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = [
            'industry',
            'services',
            'description',
            'phone_number',
            'location',
            'website_url',
            'instagram_url',
            'facebook_url',
            'telegram_url',
    
            'linkedin_url',
         
        ]
        widgets = {
             'industry': forms.TextInput(attrs={'class': 'form-control'}),
             'services': forms.Textarea(attrs={'class': 'form-control'}),
             'description': forms.Textarea(attrs={'class': 'form-control'}),
             'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
             'location': forms.TextInput(attrs={'class': 'form-control'}),
    
             'website_url': forms.TextInput(attrs={'class': 'form-control'}),
             'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
             'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
             'telegram_url': forms.TextInput(attrs={'class': 'form-control'}),
   
   
             'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
    
}
class EditEmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = [
            'industry',
            'services',
            'description',
            'phone_number',
            'location',
            'website_url',
            'instagram_url',
            'facebook_url',
            'telegram_url',
    
            'linkedin_url',
         
        ]
        widgets = {
             'industry': forms.TextInput(attrs={'class': 'form-control'}),
             'services': forms.Textarea(attrs={'class': 'form-control'}),
             'description': forms.Textarea(attrs={'class': 'form-control'}),
             'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
             'location': forms.TextInput(attrs={'class': 'form-control'}),
    
             'website_url': forms.TextInput(attrs={'class': 'form-control'}),
             'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
             'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
             'telegram_url': forms.TextInput(attrs={'class': 'form-control'}),
   
   
             'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
    
}
class EditProfilePicForm(forms.ModelForm):
   
    class Meta:
          model = ProfilePic
          fields = (
      
            'profile_pic',
           
        )
    widgets = {
      
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
        }
class CreatProfilePicForm(forms.ModelForm):
   
    class Meta:
          model = ProfilePic
          fields = (
      
            'profile_pic',
           
        )
    widgets = {
      
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
        }

class PasswordChangingForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    class Meta:
        model=User
        fields=('old_password','new_password1','new_password2')


