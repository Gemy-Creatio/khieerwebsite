from django.urls import path
from . import views


urlpatterns = [
    path('add/design', views.AddDesign, name='add-design'),
        path('all/design', views.AllDesigns.as_view(), name='all-design'),
    path('user/designs', views.AllUserDesigns.as_view(), name='user-designs'),
    path('add/user', views.addUserDesign, name='user-add'),

]