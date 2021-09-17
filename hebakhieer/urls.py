from django.urls import path
from . import views

urlpatterns = [
    path('request', views.heba_khieer, name='heba-khieer'),
    path('register/volunteer', views.register_volunteer, name='reg-vol'),
    path('dashboard/options', views.dash_options, name='dash-options'),
    path('dashboard/employees', views.dash_emps, name='dash-emps'),
    path('dashboard/hebas', views.dash_heba, name='dash-hebas'),
    path('dashboard/volunteer', views.dash_volunteer, name='all-vol')

]
