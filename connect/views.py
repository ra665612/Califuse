from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from connect.forms import ConnectForm
from connect.models import Post1, Friend

#Create your views here.
class ConnectView(TemplateView):
    template_name = 'connect/connect.html'

    def get(self, request):
        users = User.objects.order_by('username').exclude(id=request.user.id)
        try:
            friend = Friend.objects.get(current_user=request.user)
        except Friend.DoesNotExist:
            friend = Friend.objects.get_or_create(current_user=request.user)

        friends = friend.users.all()

        query = request.GET.get("q")
        if query:
            users = users.filter(
                Q(username__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
                ).distinct()

        # paginate other users
        paginator = Paginator(users, 25) # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            users = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            users = paginator.page(paginator.num_pages)

        # paginate friends
        paginator = Paginator(friends, 25) # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            friends = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            friends = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            friends = paginator.page(paginator.num_pages)


        args = {
            'users': users, 'friends': friends,
        }
        return render(request, self.template_name, args)



def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)

    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)

    return redirect('/connect')
