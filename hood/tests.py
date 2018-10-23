from django.test import TestCase
from .models import *
from .views import dashboard
from django.core.urlresolvers import reverse
from django.urls import resolve
# Create your tests here.


class HoodTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='a')
        self.new_hood = Hood(name="hot", description="anywhere",
                             admin=self.user, occupants="5")
        self.profile = Profile(user=self.user, name="a",
                               bio="xyz", email="yuo@gmail.com")
        self.bussiness = Business(
            name="game on", contact="098765", description="you are great")
        self.post = Post(user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
