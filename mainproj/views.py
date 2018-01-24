from django.shortcuts import render, redirect, render_to_response, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
from mainproj.forms import EditProfileForm, EditUserProfile
from django.core.urlresolvers import reverse, reverse_lazy
# from django.template.context import RequestContext
# from django.core.mail import EmailMessage
# from django.template import Context
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from registration.signals import user_registered
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView
from cali.models import UserProfile


from mainproj.forms import PostForm
from mainproj.models import Post


# Create your views here.

def about(request):
    return render(request, "about.html", {})

def contact(request):
    return render(request, "contact.html", {})

def faq(request):
    return render(request, "faq.html", {})

def Privacy_Policy(request):
    return render(request, "Privacy_Policy.html", {})


# class ProfileView(TemplateView):
#     template_name = 'profile.html'
#
#     def get(self, request):
#         form = PostForm()
#         posts = Post.objects.all().order_by('-created')
#         users = User.objects.exclude(id=request.user.id)
#
#         args = {
#             'form': form, 'posts': posts, 'users': users
#         }
#         return render(request, self.template_name, args)
#         # return render(request, self.template_name,{'form': form})
#
#
#     def post(self, request):
#         form = PostForm(request.POST, request.FILES or None)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.save()
#
#             text = form.cleaned_data['post']
#             form = PostForm()
#             return redirect('/profile')
#
#         args = {'form': form, 'text': text}
#         return render(request, self.template_name, args)

# def createUserProfile(request, instance, **kwargs):
#     user_profile = UserProfile.objects.create(user=instance)
def createUserProfile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
    pass


# user_registered.connect(createUserProfile)
user_registered.connect(createUserProfile, sender=User)


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            # form.save()
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = PostForm()
    else:
        form = PostForm(instance=request.user)

    posts = Post.objects.all().order_by('-created')
    users = User.objects.exclude(id=request.user.id)

    # paginate posts
    paginator = Paginator(posts, 35) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)



    args = {'user': user, 'form': form, 'posts': posts, 'users': users}
    return render(request, 'profile.html', args)

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('view_profile')

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            # return redirect(reverse('profile'))
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


def edit_user(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = EditUserProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            city = form.cleaned_data['city']
            bio = form.cleaned_data['bio']
            twitter = form.cleaned_data['twitter']
            facebook = form.cleaned_data['facebook']
            linkedin = form.cleaned_data['linkedin']

            form.save()
            # return redirect(reverse('home'))
            return redirect('/profile')

    else:
        form = EditUserProfile(instance=profile)
    return render(request, 'edit_user.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('profile'))
        else:
            return redirect(reverse('accounts/password_change_form.html'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/password_change_done.html', args)
