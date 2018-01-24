from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    image = models.ImageField(upload_to='profile_image', default='default_user.png', blank=True, null=True)
    backimage = models.ImageField(upload_to='profile_image', default='default_user.png', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)
