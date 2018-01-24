from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def home(request):
    title = "Hello"

    context = {
         "title": title,
     }

    return render(request, "home.html", {})

def contact(request):
    context = {
        "form": form,
    }
    return render(request, "forms.html", context)



# def connect(request):
#     return render(request, "connect.html",{})

# class ConnectView(TemplateView):
#     template_name='connect.html'
