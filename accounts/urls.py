from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register-trainer', views.register_trainer, name='register-trainer'),
    path('register-employee', views.register_secondary_empolyee, name='register-employee'),
    path('register-helper-emplyeer', views.register_helper_employee, name='register-helper'),
    path('register-volunteer', views.register_volunteer, name='reg-vol'),
    path('user-profile', views.user_profile, name='user-profile'),
    path('user-profile-dash', views.user_profile_dash, name='user-profile-dash'),
    path('<int:pk>', views.edit_user_info, name='edit-info'),
    path('employees/list', views.employees_list, name='emp-list'),

]
