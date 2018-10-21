from django.shortcuts import redirect, render
# Create your views here.


def home(request):

    welcome = "welcome to the home page"
    return render(request, 'hood/home.html', {"welcome": welcome})
