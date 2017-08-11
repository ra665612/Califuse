from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import password_reset, password_reset_done
from mainproj.views import ProfileView
from . import views

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'joins.views.home', name='home'),
    url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'),
    url(r'^about/$', 'mainproj.views.about', name='about'),
    url(r'^contact/$', 'mainproj.views.contact', name='contact'),
    url(r'^faq/$', 'mainproj.views.faq', name='faq'),
    # url(r'^connect/$', 'mainproj.views.connect', name='connect'),
    url(r'^Privacy_Policy/$', 'mainproj.views.Privacy_Policy', name='Privacy_Policy'),
    url(r'^profile/$',ProfileView.as_view(), name='profile'),
    # url(r'^profile/(?P<pk>\d+)/$', 'mainproj.view_profile', name='view_profile_with_pk'),
    url(r'^profile/edit/$', 'mainproj.views.edit_profile', name='edit_profile'),
    url(r'^connect/$', include('connect.urls'), name='connect'),
    # url(r'^blog/', nclude('blog.urls')),
    url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'),


    url(r'^accounts/', include('registration.backends.default.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
