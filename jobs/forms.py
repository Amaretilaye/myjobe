from django import forms
from .models import Applicant,Categories,Job
from django.forms import ClearableFileInput
from django.contrib.auth import get_user_model


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['resume', 'cover_letter']

class JobPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Categories.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Job
        fields = [
            'title', 'category', 'description', 'location', 'salary', 
            'application_deadline', 'requirements', 'responsibilities', 
            'education_requirements', 'job_type', 'experience','is_featured'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'application_deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'responsibilities': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'education_requirements': forms.TextInput(attrs={'class': 'form-control'}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class JobEditForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Categories.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Job
        fields = [
            'title', 'category', 'description', 'location', 'salary', 
            'application_deadline', 'requirements', 'responsibilities', 
            'education_requirements', 'job_type', 'experience','is_featured'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'application_deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'responsibilities': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'education_requirements': forms.TextInput(attrs={'class': 'form-control'}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
