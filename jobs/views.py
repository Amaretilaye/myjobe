from django.shortcuts import render,get_object_or_404,redirect,reverse 
from django.views.generic import* # Corrected import statement
from .models import Categories,Job,Applicant
from django.db.models import Q
from datetime import timedelta
from django.utils import timezone
from .forms import ApplicantForm,JobPostForm,JobEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count
from django.views.generic import TemplateView
from wkhtmltopdf.views import PDFTemplateView

class ApplicantPDFView(PDFTemplateView):


    template_name = 'users/my_applicationss.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['applicants'] = Applicant.objects.all()  # Fetch all applicants
        return context


class IndexView(ListView):
    template_name = 'home.html'
    model = Categories  # Using the Categories model as the primary model
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all().order_by('-posted_date')[:10]    
        search_query = self.request.GET.get('search')
        if search_query:
            posts = Job.objects.filter(title__icontains=search_query)
            context['search_query'] = search_query
            context['jobs'] = jobs
        return context
class SearchView(ListView):
    template_name = 'search_results.html'
    model = Job

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        if search_query:
            return Job.objects.filter(title__icontains=search_query)
        return Job.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('search')
        if search_query:
            jobs = Job.objects.filter(title__icontains=search_query)
            context['search_query'] = search_query
            context['jobs'] = jobs
        return context

class CategoryDetailView(DetailView):
    model = Categories
    template_name = 'category_detail.html'

    
     
    

class JobListView(ListView):
    model = Job
    template_name = 'job_listing.html'
    paginate_by= 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_jobs'] = Job.objects.count()  # Get the total count of jobs
        return context


 
    

class JobDetailView(DetailView):
    model = Job
    template_name = 'job_details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now().strftime("%Y-%m-%d")
        return context

@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    form = ApplicantForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        applicant = form.save(commit=False)
        applicant.user = request.user.employee
        applicant.job = job
        applicant.save()
        return redirect('job_detail', pk=job_id)

    return render(request, 'apply_for_job.html', {'form': form, 'job': job})

def my_applications(request):
    # Retrieve applications for the logged-in user
    applications = Applicant.objects.filter(user=request.user.employee)
    return render(request, 'my_applications.html', {'applications': applications})
class JobEditView(UpdateView):
    model = Job
    template_name = 'users/job_edit_form.html'
    form_class = JobEditForm
    success_url = reverse_lazy('my_job_list') 

class JobPostView(LoginRequiredMixin,FormView):
    template_name = 'users/job_post_form.html'
    form_class = JobPostForm


    def form_valid(self, form):
        job_post = form.save(commit=False)
        job_post.company = self.request.user.employerprofile
        
        # Assuming you have a field named 'catagory' in your form that corresponds to the 'catagory' ForeignKey in the Job model
        job_post.catagory = form.cleaned_data['category']  
        
        job_post.save()

        # Display success message
        messages.success(self.request, 'Job posted successfully!')

        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the desired URL after successful form submission
        return reverse_lazy('post_job')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add additional context data if needed
        return context

#class ApplicantView(ListView):
    #model = Applicant
    #template_name ='users/my_applicants.html'
    #context_object_name = 'applicants'



def all_applicants(request):
    applicants = Applicant.objects.all()
    return render(request, 'users/all_applicants.html', {'applicants': applicants})

def job_applicants(request):
    applicants = Applicant.objects.filter(status='applied')
    return render(request, 'users/my_applicants.html', {'applicants': applicants})

def shortlisted_applicants(request):
    applicants = Applicant.objects.filter(status='shortlisted')
    return render(request, 'users/shortlisted_applicants.html', {'applicants': applicants})

def rejected_applicants(request):
    applicants = Applicant.objects.filter(status='rejected')
    return render(request, 'users/rejected_applicants.html', {'applicants': applicants})

    

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'users/job_confirm_delete.html'  # Create this template to show a confirmation dialog
    success_url = reverse_lazy('my_job_list')  # Re

class MyJobListView(ListView):
    model = Job
    template_name = 'users/my_job_list.html'
    context_object_name = 'joblist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the logged-in employer
        logged_in_employer = self.request.user.employerprofile

        # Get count of jobs posted by the logged-in employer
        context['employer_job_count'] = Job.objects.filter(company=logged_in_employer).count()
        
        # Annotate each job with the number of applicants
        context['joblist'] = Job.objects.annotate(num_applicants=Count('applicant'))

        return context
class UpdateStatusView(View):
    
    def post(self, request, applicant_id):
        applicant = get_object_or_404(Applicant, id=applicant_id)
        new_status = request.POST.get('status')
        
        # Check if the auto_submit field is present to automatically update status
        if request.POST.get('auto_submit'):
            applicant.status = new_status
            applicant.save()
            
            # Add a success message if desired
            
        
        # Redirect back to the ApplicantDetailView for the same applicant
        return redirect(reverse('applicant-detail', args=[applicant_id]))

class ApplicantDetailView(DetailView):
    model = Job  # This should point to the Job model since you want to view applicants related to a job.
    template_name = 'users/applicant_detail.html'
    context_object_name = 'job'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['applicants'] = self.object.applicant_set.all()  # This assumes the related name in the Applicant model is 'applicant_set'
        return context

def shortlisted_applicants(request):
    applicants = Applicant.objects.filter(status='shortlisted')
    return render(request, 'users/shortlisted_applicants.html', {'applicants': applicants})

def rejected_applicants(request):
    applicants = Applicant.objects.filter(status='rejected')
    return render(request, 'users/rejected_applicants.html', {'applicants': applicants})

    

