from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views
from .models import *
from .views import home, profile

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^profile$', profile, name='profile'),
]
