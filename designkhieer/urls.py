from django.urls import path
from . import views


urlpatterns = [
    path('add/design', views.AddDesign.as_view(), name='add-design'),
    path('all/design', views.AllDesigns.as_view(), name='all-design'),
    path('user/designs', views.AllUserDesigns.as_view(), name='user-designs'),
    path('add/user', views.AddDesign.as_view(), name='user-add'),
    path('delete/cesign/<int:pk>', views.DeleteDesign, name='delete-design'),
    path('user/new', views.NewUserDesign.as_view(), name='new-designs'),
    path('ajax/new', views.AddUserRequestDesign, name='req-design'),

]