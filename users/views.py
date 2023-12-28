
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django. views.generic import DetailView,View ,CreateView,UpdateView,ListView
from django.views import generic 
from django.contrib .auth.views import PasswordChangeView
from django.urls import reverse_lazy
#from .forms import EditProfileForm,PasswordChangingForm, ProfilePageForm,EditProfilepageForm
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import EmployerSignUpForm, EmployeeSignUpForm,EditProfileForm,ProfilePageForm,PasswordChangingForm,EditProfilePicForm, CreatProfilePicForm
from .forms import EmployerProfileForm,EditEmployerProfileForm,JobPostForm
from django.contrib.auth.forms import AuthenticationForm 
from .models import User,Employer,Employee
from jobs.models import EmployeeProfile,ProfilePic,EmployerProfile,Applicant,Job,My_applicant
from jobs.models import*
from .models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect

def register(request):
    return render(request, 'users/register.html')

class employer_register(CreateView):
    model = User
    #fields= '__all__'
    form_class = EmployerSignUpForm
    template_name = 'users/employer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class employee_register(CreateView):
    model = User
    #fields='__all__'
    form_class = EmployeeSignUpForm
    template_name = 'users/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password or the account is inactive.")
        else:
            messages.error(request, "Invalid username or password. Please check your input.")

    return render(request, 'users/login.html', {'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')


# Create your views here.

def users_admin(request):
    return render(request, 'users/admin_dashbord.html')
def users_employee(request):
    return render(request, 'users/employee_dashbord.html')
def users_employer(request):
    return render(request, 'users/employer_dashbord.html')
def users(request):
    return render(request, 'users/index.html')
def user_profile(request):
    return render(request, 'users/users-profile.html')

class CreatProfilePageView(CreateView):
    
    model=EmployeeProfile
    form_class= ProfilePageForm
    success_url=reverse_lazy('dashbord')
    template_name='users/create_user_profile.html'
    #fields='__all__'
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(). form_valid(form)
class CreatEmployerProfileView(CreateView):
    
    model=EmployerProfile
    form_class=EmployerProfileForm
    success_url=reverse_lazy('dashbord')
    template_name='users/creat_employer_profile.html'
    #fields='__all__'
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(). form_valid(form)

class EditEmployerProfileView(UpdateView):
    model = EmployerProfile
    template_name = 'users/edit_employer_Profile.html'
    form_class = EditEmployerProfileForm

    def get_success_url(self):
        # Use reverse_lazy to dynamically generate the URL based on the current view
        return reverse_lazy('edit_employer_profile', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # Add a success message
        messages.success(self.request, 'Successfully updated your profile!')

        return super().form_valid(form)
class EditProfilePageView(UpdateView):
    model = EmployeeProfile
    template_name = 'users/edit_user_Profile.html'
    form_class = EditProfileForm

    def get_success_url(self):
        # Use reverse_lazy to dynamically generate the URL based on the current view
        return reverse_lazy('edit_user_profile', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # Add a success message
        messages.success(self.request, 'Successfully updated your profile!')

        return super().form_valid(form)
    
class CreatProfilepicView(CreateView):
    
    model=ProfilePic
    form_class= CreatProfilePicForm
    success_url=reverse_lazy('dashbord')
    template_name='users/creat_profile_pic.html'
    #fields='__all__'
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(). form_valid(form)
class EditProfilePicview(UpdateView):
    model =ProfilePic
    template_name = 'users/change_profile_pic.html'
    form_class = EditProfilePicForm
    success_url=reverse_lazy('dashbord')


    
class EmployeeProfileListView(ListView):
    model = EmployeeProfile
    template_name = 'users/users-profile.html'  # Your template name
    context_object_name = 'user_profiles'  # The name used in the template for the list

    def get_queryset(self):
   
        # Customize the queryset based on your needs
     return EmployerProfile.objects.all()
    
@method_decorator(login_required, name='dispatch')
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password-success')
    template_name = 'users\change_password.html'

    def form_valid(self, form):
        messages.success(self.request, 'Password successfully changed.')
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the same page after a successful password change
        return reverse_lazy('password-change')

def my_applications(request):
    # Retrieve applications for the logged-in user
    applications = Applicant.objects.filter(user=request.user.employee)
    return render(request, 'users/my_applications.html', {'applications': applications})

def view_my_applicants(request):
    # Fetch jobs posted by the logged-in employer
    jobs = Job.objects.filter(company=request.user.employerprofile)  # Assuming you have a relationship between User and EmployerProfile
    applicants_by_job = {}
    for job in jobs:
        applicants_by_job[job] = job.my_applicants.all()

    return render(request, 'users/my_applicants.html', {'applicants_by_job': applicants_by_job})

class JobPostView(FormView):
    model= Job
    template_name = 'users/job_post_form.html'
    form_class = JobPostForm
   

    def form_valid(self, form):
        job_post = form.save(commit=False)
        job_post.company = self.request.user.employerprofile
        job_post.save()

        # Display success message
        messages.success(self.request, 'Successfully posted your job!')

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add additional context data if needed
        return context
    def get_success_url(self):
        # Use reverse_lazy to dynamically generate the URL based on the current view
        return reverse_lazy('post_job')

    def form_valid(self, form):
        # Add a success message
        messages.success(self.request, ' job posted seccesfuly!')
        return super().form_valid(form)
 