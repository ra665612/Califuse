from django.conf.urls import url
from connect.views import ConnectView

urlpatterns = [
    url(r'^$',ConnectView.as_view(), name='connect'),
    # url(r'^profile/(?P<pk>\d+)/$', 'connect.view_profile', name='view_profile_with_pk'),
]
