from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('about', views.about_page, name='about-page'),
    path('ethics', views.ethics_page, name='ethics-page'),
    path('roaya', views.roaya_page, name='roaya-page'),
    path('khieer30', views.khieer30_page, name='khieer30-page'),
    path('staff', views.staff_page, name='staff-page'),
    path('paramg', views.paramg_page, name='paramg-page'),
    path('autoservices', views.autoservices, name='auto-page'),
    path('support', views.tech_support, name='tech-page'),

]
