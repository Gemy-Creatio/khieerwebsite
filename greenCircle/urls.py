from django.urls import path
from . import views

urlpatterns = [
    path('greenCircle', views.greenCircle, name='green-circle'),
    path('greenCourse/<int:pk>', views.greenCircleCourses, name='green-courses'),
    path('greenTrainer/<int:pk>', views.green_trainer_details, name='green-trainer'),
    path('greenCourse/add/<int:pk>', views.course_request, name='green-add-user')

]
