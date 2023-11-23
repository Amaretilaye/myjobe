from django.urls import path
from .views import IndexView,JobListView
from. import views

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
       #job
    path('jobs/', JobListView.as_view(), name='job-list'),
  

]
