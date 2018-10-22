from django.shortcuts import redirect, render, get_object_or_404
from .forms import ProfileForm, Hoodform, BusinessForm
from django.contrib.auth.decorators import login_required
from .models import Hood
from urllib import request

# Create your views here.


def home(request):
    current_user = request.user
    print(current_user)
    if request.method == 'POST':
        formhood = Hoodform(request.POST)
        if formhood.is_valid():
            upload = formhood.save(commit=False)
            upload.admin = current_user
            upload.save()
            return redirect('home')
    else:

        formhood = Hoodform()
    welcome = "welcome to the home page"

    hoods = Hood.objects.all()
    return render(request, 'hood/home.html', {"welcome": welcome, "formhood": formhood, "hoods": hoods})
