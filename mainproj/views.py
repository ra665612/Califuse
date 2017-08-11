from django.shortcuts import render, redirect
from mainproj.forms import EditProfileForm
from django.core.urlresolvers import reverse
# from django.template.context import RequestContext
# from django.core.mail import EmailMessage
# from django.template import Context
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from registration.signals import user_registered
from django.views.generic import TemplateView


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

# def view_profile(request, pk=None):
#     if pk:
#         user = User.objects.get(pk=pk)
#     else:
#         user = request.user
#     args = {'user': user}
#     return render(request, 'profile.html', args)


class ProfileView(TemplateView):
    template_name = 'profile.html'

    # def view_profile(request, pk=None):
    #     if pk:
    #         user = User.objects.get(pk=pk)
    #     else:
    #         user = request.user
    #         args = {'user': user}
    #     return render(self.template_name, args)

    def get(self, request):
        form = PostForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)

        args = {
            'form': form, 'posts': posts, 'users': users
        }
        return render(request, self.template_name, args)
        # return render(request, self.template_name,{'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = PostForm()
            return redirect('/profile')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


    # def remove_items(request):
    # if request.method == 'POST':
    #     form = PostForm()
    #     profileview = ProfileView.objects.all()
    #     item_id = int(request.POST.get('item_id'))
    #     item = Inventory.objects.get(id=item_id)
    #     item.delete()
    #     return render_to_response('inventory.html', {
    #         'form':form, 'inventory':inventory,
    #         }, RequestContext(request))


def createUserProfile(sender, instance,**kwargs):
    user_profile = UserProfile.objects.create(user=instance)

user_registered.connect(createUserProfile)

# def view_profile(request, pk=None):
#     if pk:
#         user = User.objects.get(pk=pk)
#     else:
#         user = request.user
#     args = {'user': user}
#     return render(request, 'profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)

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
