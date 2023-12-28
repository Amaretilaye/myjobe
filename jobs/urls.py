from django.urls import path
from .views import IndexView,JobListView,JobDetailView,apply_for_job
from. import views

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
       #job
    path('jobs/', JobListView.as_view(), name='job-list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    #path('jobs/<int:job_id>/', ApplyForJobView.as_view(), name='apply_for_job'),
    path('apply/<int:job_id>/', apply_for_job, name='apply_for_job'),
    
  

]
