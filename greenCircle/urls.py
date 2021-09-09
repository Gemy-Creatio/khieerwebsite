from django.urls import path
from . import views

urlpatterns = [
    path('greenCircle', views.greenCircle, name='green-circle')
]
