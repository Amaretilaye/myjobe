from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import* # Corrected import statement
from .models import Categories,Job,Applicant
from django.db.models import Q
from datetime import timedelta
from django.utils import timezone

class IndexView(ListView):  # Corrected class name
   template_name = 'home.html'
   model= Categories


class JobListView(ListView):
    model = Job
    template_name = 'job_listing.html'
    
    paginate_by = 10

    def get_queryset(self):
        # Check if job type, category, and date range parameters are provided in the URL
        location = self.request.GET.get('locations', None)
        job_type = self.request.GET.get('job_type', None)
        category = self.request.GET.get('category', None)
        date_range = self.request.GET.get('date_range', None)

        # Build the filter criteria based on provided parameters
        filter_criteria = Q(is_featured=True)
        if job_type:
            filter_criteria &= Q(job_type=job_type)
        if category:
            filter_criteria &= Q(category__name=category)
        if location:
            filter_criteria &= Q(location__name=location)

        # Apply date range filter if provided
        if date_range == '0-1':
            filter_criteria &= Q(posted_date__gte=timezone.now() - timedelta(days=1))
        elif date_range == '1-2':
            filter_criteria &= Q(posted_date__gte=timezone.now() - timedelta(days=2), posted_date__lt=timezone.now() - timedelta(days=1))
        # Add more conditions for other date ranges as needed

        # Apply filters to the queryset
        return Job.objects.filter(filter_criteria)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the list of unique categories and job types to the context
        context['categories'] = Categories.objects.all()
        context['job_types'] = Job.JOB_TYPE_CHOICES
        context['locations'] = Job.LOCATION_CHOICES
        return context
class JobDetailView(DetailView):
    model = Job
    template_name = 'job_details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now().strftime("%Y-%m-%d")
        return context


class ApplyForJobView(View):
    template_name = 'jobs/apply_for_job.html'

    def get(self, request, job_id):
        job = get_object_or_404(Job, pk=job_id)
        form = Applicant
        return render(request, self.template_name, {'form': form, 'job': job})

    def post(self, request, job_id):
        job = get_object_or_404(Job, pk=job_id)
        form = Applicant(request.POST, request.FILES)

        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.user.employer = request.user.employer
            applicant.job = job
            applicant.save()
            return redirect('job_detail', job_id=job_id)

        return render(request, self.template_name, {'form': form, 'job': job})

