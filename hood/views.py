from django.shortcuts import redirect, render, get_object_or_404
from .forms import ProfileForm, Hoodform, BusinessForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):

    welcome = "welcome to the home page"
    return render(request, 'hood/home.html', {"welcome": welcome})
