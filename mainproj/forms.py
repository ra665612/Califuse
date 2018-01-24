from django import forms
from mainproj.models import Post
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.requests import RequestSite
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.template import loader
from cali.models import UserProfile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class EditProfileForm(UserChangeForm):
    template_name='edit_profile'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )

class EditUserProfile(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = [
            'image',
            'backimage',
            'bio',
            'city',
            'facebook',
            'twitter',
            'linkedin'
        ]
        labels = {
            'image': 'Profile image',
            'backimage': 'Header image',
            'facebook': 'Facebook username',
            'twitter': 'Twitter username',
            'linkedin': 'Linkedin username'
        }
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'post',
            'image',
        ]
        labels = {
            'post': '',
            'image': 'Attach an Image'
        }
        widgets = {
            'post': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
