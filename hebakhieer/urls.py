from django.urls import path
from . import views

urlpatterns = [
    path('request', views.heba_khieer, name='heba-khieer')
]
