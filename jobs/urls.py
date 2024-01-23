from django.urls import path
from .views import IndexView,JobListView,JobDetailView,apply_for_job,JobPostView,CategoryDetailView,SearchView
from .views import MyJobListView,ApplicantDetailView,UpdateStatusView,ApplicantPDFView,all_applicants
from .import views
from .views import*
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
       #job
    path('jobs/', JobListView.as_view(), name='job-list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    #path('jobs/<int:job_id>/', ApplyForJobView.as_view(), name='apply_for_job'),
    path('apply/<int:job_id>/', apply_for_job, name='apply_for_job'),
    path('users/post_job/', JobPostView.as_view(), name='post_job'),
    path('users/<int:pk>/edit_job/', JobEditView.as_view(), name='edit_job'),
    #path('category/', CategoryDetailView.as_view(), name='category-detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'), 
    path('search/', SearchView.as_view(), name='search_results'),
    path('users/my_applicants/', views.job_applicants, name='my_applicants'),
    path('users/shortlisted/', views.shortlisted_applicants, name='shortlisted_applicants'),
    path('users/rejected/', views.rejected_applicants, name='rejected_applicants'),
    path('users/my_job_list/', MyJobListView.as_view(), name='my_job_list'),
    path('users/applicants/<int:pk>/', ApplicantDetailView.as_view(), name='applicant-detail'),
    
    #path('users/update_status/<int:applicant_id>/', UpdateStatusView.as_view(), name='update_status'),
    path('users/update_status/<int:applicant_id>/', views.UpdateStatusView.as_view(), name='update_status'),
    path('users/shortlisted/', views.shortlisted_applicants, name='shortlisted_applicants'),
    path('users/rejected/', views.rejected_applicants, name='rejected_applicants'),
    path('users/all_applicants', views.all_applicants, name='all_applicants'),
    path('users/applicants_pdf/', ApplicantPDFView.as_view(), name='applicants_pdf'),
    path('users/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
   

    

   

  

]
