from django.shortcuts import redirect, render, get_object_or_404
from .forms import ProfileForm, Hoodform, BusinessForm
from django.contrib.auth.decorators import login_required
from .models import Hood, Profile, Business
from urllib import request


# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    # current_user = request.user.profile
    # print(current_user)
    if request.method == 'POST':
        formhood = Hoodform(request.POST, request.FILES)
        if formhood.is_valid():
            upload = formhood.save(commit=False)
            upload.admin = request.user.profile
            request.user.profile.save()
            upload.save()
            return redirect('home')
    else:

        formhood = Hoodform()
    welcome = "welcome to the home page"

    hoods = Hood.objects.all()
    return render(request, 'hood/home.html', {"welcome": welcome, "formhood": formhood, "hoods": hoods})
