from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import password_reset, password_reset_done
# from mainproj.views import ProfileView
from mainproj.views import PostDelete
from . import views
from django.views.generic import RedirectView

urlpatterns = [

    url(r'^$', 'cali.views.home', name='home'),
    # url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'),
    url(r'^about/$', 'mainproj.views.about', name='about'),
    url(r'^contact/$', 'mainproj.views.contact', name='contact'),
    url(r'^faq/$', 'mainproj.views.faq', name='faq'),
    # url(r'^connect/$', 'mainproj.views.connect', name='connect'),
    url(r'^Privacy_Policy/$', 'mainproj.views.Privacy_Policy', name='Privacy_Policy'),
    # url(r'^profile/$',ProfileView.as_view(), name='profile'),
    url(r'^profile/$', 'mainproj.views.view_profile', name='view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', 'mainproj.views.view_profile', name='view_profile_with_pk'),
    url(r'^profile/edit/$', 'mainproj.views.edit_profile', name='edit_profile'),
    url(r'^profile/edit_user/$', 'mainproj.views.edit_user', name='edit_user'),
    url(r'^profile/edit/password/$', RedirectView.as_view(url='http://califuse.com/accounts/password/change')),
    url(r'^connect/$', include('connect.urls'), name='connect'),
    # url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'),
    url(r'^profile/(?P<pk>[0-9]+)/delete/$', PostDelete.as_view(), name='post-delete'),

    url(r'^friend/(?P<operation>.+)/(?P<pk>\d+)/$', 'connect.views.change_friends', name='change_friends'),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
