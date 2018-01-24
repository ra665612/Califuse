from django.db import models
from django.contrib.auth.models import User

# models here

class Post(models.Model):
    # post = models.CharField(max_length=500)
    post = models.TextField(max_length=500)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='profile_image', blank=True, null=True)
    # post_pic = models.ImageField(upload_to='profile_image', blank=True, null=True)
    # post_pic = models.ImageField(upload_to='profile_image', blank=True)

    def __unicode__(self):
        return self.user;
