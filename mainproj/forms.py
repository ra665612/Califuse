from django import forms
from mainproj.models import Post
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.requests import RequestSite
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.template import loader


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )

class PostForm(forms.ModelForm):
    # image = forms.ImageField
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'cols': 20,
            'rows': 20,
            'class': 'form-control',
            'placeholder': 'Write a post...',
            'style': 'font-size: 1em',
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)
