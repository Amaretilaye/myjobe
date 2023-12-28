from django.db import models
from django .urls import reverse
from users.models import*
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Categories(models.Model):
    cat_icon = models.ImageField(upload_to='icons/')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')

    def get_post_count(self):
        return self.posts.count()

class EmployeeProfile(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='images/profile/', blank=True, null=True)
    web_site_url = models.CharField(max_length=100, blank=True, null=True)
    instagram_url = models.CharField(max_length=100, blank=True, null=True)
    facebooke_url = models.CharField(max_length=100, blank=True, null=True)
    telegram_url = models.CharField(max_length=100, blank=True, null=True)
    
    # Use ManyToManyField for skills
    skills = models.ManyToManyField(Categories, blank=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    certifications = models.CharField(max_length=255, blank=True, null=True)
    languages = models.CharField(max_length=255, blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')
    
class EmployerProfile(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number=models.IntegerField( blank=True, null=True)
    location=models.TextField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    services = models.TextField(blank=True, null=True)
    website_url = models.CharField(max_length=100, blank=True, null=True)
    instagram_url = models.CharField(max_length=100, blank=True, null=True)
    facebook_url = models.CharField(max_length=100, blank=True, null=True)
    telegram_url = models.CharField(max_length=100, blank=True, null=True)
    # Use ManyToManyField for categories (assuming Categories is a model for company categories)
    linkedin_url = models.URLField(blank=True, null=True)
 

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')
    
class ProfilePic(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/profile/', blank=True, null=True)

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('freelance', 'Freelance'),
        ('permanent', 'Permanent'),
        ('contract', 'Contract'),
        ('remote', 'Remote'),
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
    ]

    LOCATION_CHOICES = [
        ('city1', 'City 1'),
        ('city2', 'City 2'),
        ('city3', 'City 3'),
        # Add more cities as neededs
    ]

    company = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
    company_logo = models.ImageField(upload_to='images/profile/', blank=True, null=True)
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(Categories)
    description = models.TextField()
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)
    education_requirements = models.CharField(max_length=100, blank=True, null=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    experience = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.title)
class Applicant(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    cover_letter = models.TextField(blank=True, null=True)
    applied_date = models.DateTimeField(auto_now_add=True)
    is_shortlisted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    #STATUS_CHOICES = [
        #('applied', 'Applied'),
       # ('shortlisted', 'Shortlisted'),
       # ('rejected', 'Rejected'),
    #]
    #status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='applied')
    def __str__(self):
        return f"{self.user.username} - {self.job.title} Application"
    
# No changes needed here
class My_applicant(models.Model):
    job = models.ForeignKey(Job, related_name='applicants', on_delete=models.CASCADE)
    # Add other fields related to the applicant like name, resume, etc.
    
    def __str__(self):
        return f"{self.job.title} - {self.id}"
