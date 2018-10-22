from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from .views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
