from django.urls import path
from .views import*
from. import views
from.views import CreatProfilePageView,EditProfilePageView,EmployeeProfileListView

urlpatterns = [
    path('', views.users, name='dashbord'),
    path('w_admin/', views.users_admin, name='w-admin'),
    path('employee/', views.users_employee, name='employee'),
    path('employer/', views.users_employer, name='employer'),
    path('user-profile/', views.user_profile, name='user_profile'),

    
    path('register/',views.register, name='register'),
    path('employer_register/',views.employer_register.as_view(), name='employer_register'),
    path('employee_register/',views.employee_register.as_view(), name='employee_register'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),

     #profile employee 
    path('profile/',EmployeeProfileListView.as_view(), name='employee_profile'),
    path('create-user-profile/',CreatProfilePageView.as_view(), name='create_user_profile'),
    path('create-profile_pic/',CreatProfilepicView.as_view(), name='create_profile_pic'),
    path('<int:pk>/edit-user-profile/', EditProfilePageView.as_view(), name='edit_user_profile'),
    path('<int:pk>/change-profile-pic/', EditProfilePicview.as_view(), name='change_profile_pic'),
    path('password/',PasswordsChangeView.as_view(template_name='users/change_password.html'), name="password-change"),
    #path('password_success/',views.password_success,name='password-success'),

    #profile of employer 
    path('create-employer-profile/',CreatEmployerProfileView.as_view(), name='create_employer_profile'),
    path('<int:pk>/edit-employer-profile/', EditEmployerProfileView.as_view(), name='edit_employer_profile'),


 

    


]

    

