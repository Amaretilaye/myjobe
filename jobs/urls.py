from django.urls import path
from .views import IndexView,JobListView,JobDetailView
from. import views

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
       #job
    path('jobs/', JobListView.as_view(), name='job-list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
  

]
