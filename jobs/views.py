from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import* # Corrected import statement
from .models import Categories,Job,Applicant
from django.db.models import Q
from datetime import timedelta
from django.utils import timezone
from .forms import ApplicantForm
from users.forms import JobPostForm



class IndexView(ListView):  # Corrected class name
   template_name = 'home.html'
   model= Categories


class JobListView(ListView):
    model = Job
    template_name = 'job_listing.html'
    paginate_by = -10

class JobDetailView(DetailView):
    model = Job
    template_name = 'job_details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now().strftime("%Y-%m-%d")
        return context


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