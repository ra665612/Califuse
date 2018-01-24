from django.conf.urls import url
from connect.views import ConnectView
from . import views


urlpatterns = [
    url(r'^$',ConnectView.as_view(), name='connect'),
    # url(r'^friend/(?P<operation>.+)/(?P<pk>\d+)/$', 'connect.views.change_friends', name='change_friends'),
]
