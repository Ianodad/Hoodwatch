from django.shortcuts import redirect, render, get_object_or_404
from .forms import ProfileForm, Hoodform, BusinessForm
from django.contrib.auth.decorators import login_required
from .models import Hood
# Create your views here.


def home(request):
    current_user = request.user

    if request.method == 'POST':
        form = Hoodform(request.POST)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.admin = current_user
            upload.save()
            return redirect('home')
    else:
        formhood = Hoodform()
    welcome = "welcome to the home page"

    hoods = Hood.objects.all()
    return render(request, 'hood/home.html', {"welcome": welcome, "formhood": formhood, "hoods": hoods})
