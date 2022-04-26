from django.urls import path
from . import views

urlpatterns = [
    path('greenCircle', views.greenCircle, name='green-circle'),
    path('greenCourse/<int:pk>', views.greenCircleCourses, name='green-courses'),
    path('greenTrainer/<int:pk>', views.green_trainer_details, name='green-trainer'),
    path('greenCourse/add/<int:pk>', views.CourseRequestView.as_view(), name='green-add-user'),
    path('greenCircle/add', views.add_greenCourse, name='register-greenCircle'),
    path('greenCircle/list', views.Greencourses_list, name='all-green'),
    path('greenCircle/requests', views.Greenrequest_list, name='all-requests'),
    path('greenCircle/trainers', views.Greentrainers_list, name='all-trainers'),
    path('document/download/list', views.Document_List, name='download-list'),
    path('document/create', views.CreateDocumentDownload.as_view(), name='create_document'),
    path('green/survey/create', views.CreateGreenSurvey.as_view(), name='create_survey'),
    path('trip/add', views.CreateVolunteerTripRequest.as_view(), name='trip-add'),
    path('trip/list', views.trip_request_list, name='trip-list'),
    path('all/topics/<int:pk>', views.GreenTopicView.as_view(), name='all-topics'),
    path('topics/<int:pk>', views.GreenTopicDetailView.as_view(), name='topic-details'),
    path('add/topic/<int:pk>', views.AddUserToTopic, name='add-topic'),
    path('all/msgs', views.AllmessagesForJoiner.as_view(), name='all-msgs'),
    path('create/topic/survery', views.CreateTopicSurvery.as_view(), name='topic-survey'),
    path('create/finish-circle/survery', views.CreateFinsihCircleView.as_view(), name='finish-circle'),

]
