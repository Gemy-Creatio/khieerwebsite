from django.urls import path
from . import views


urlpatterns = [
    path('add/design', views.AddDesign.as_view(), name='add-design'),
    path('all/design', views.AllDesigns.as_view(), name='all-design'),
    path('bag/design', views.NewUserDesignBag.as_view(), name='bag-design'),
    path('shirt/design', views.NewUserDesignShirt.as_view(), name='shirt-design'),
    path('add/user', views.AddDesign.as_view(), name='user-add'),
    path('delete/cesign/<int:pk>', views.DeleteDesign, name='delete-design'),
    path('user/new', views.AllUserDesigns.as_view(), name='new-designs'),
    path('ajax/new', views.AddUserRequestDesign, name='req-design'),
    path('join/designer', views.JoinDesigner.as_view(), name='join-designer'),
    path('accept/policy/<int:pk>', views.AcceptPpolicy.as_view(), name='accept-policy'),
    path('all/requests/', views.AllDesignRequest.as_view(), name='design-requests'),

]