from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from connect.forms import ConnectForm
from connect.models import Post1

#Create your views here.
class ConnectView(TemplateView):
    template_name = 'connect/connect.html'

    def get(self, request):
        form = ConnectForm()
        users = User.objects.exclude(id=request.user.id)
        # friend = Friend.objects.get(current_user=request.user)
        # friends = friend.users.all()

        args = {
            'form': form, 'users': users,
        }
        return render(request, self.template_name, args)

# def view_profile(request, pk=None):
#     if pk:
#         user = User.objects.get(pk=pk)
#     else:
#         user = request.user
#         args = {'user': user}
#     return render('profile.html', args)
