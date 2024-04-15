from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^video_feed/$',views.video_feed,name='video_feed'),
        url(r'^home/$',views.home,name='home'),
        url(r'^left/$',views.left,name='left'),
        url(r'^right/$',views.right,name='right'),
        url(r'^forward/$',views.forward,name='forward'),
        url(r'^backward/$',views.backward,name='backward'),
        url(r'^forward_right/$',views.forward_right,name='forward_right'),
        url(r'^forward_left/$',views.forward_left,name='forward_left'),
        url(r'^reverse_right/$',views.reverse_right,name='reverse_right'),
        url(r'^reverse_left/$',views.reverse_left,name='reverse_left'),
        url(r'^brake/$',views.brake,name='break'),
        url(r'^data/$',views.data,name='data'),
        ]
