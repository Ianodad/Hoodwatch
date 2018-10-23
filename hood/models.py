from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField
import datetime


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Hood(models.Model):
    name = models.TextField()
    image = ImageField(
        manual_crop='1280x720')
    admin = models.ForeignKey("Profile", related_name='hoods', null=True)
    description = models.TextField(default='Random group')
    location = models.ForeignKey(Location, null=True)
    datecreated = models.DateField(auto_now_add=True)
    occupants_count = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(default="Your Name")
    prof_pic = ImageField(
        manual_crop='200x200')
    bio = models.TextField(default="Tell us something")
    hoodwatch = models.ForeignKey(
        Hood, blank=True, null=True, related_name='people')
    email = models.EmailField(max_length=75, null=True)

    def __str__(self):
        return f'Profile {self.user}'

    @classmethod
    def get_profile(cls, name):
        profile = Profile.objects.filter(name=name)
        return profile


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except Exception as error:
            print(error)


class Business(models.Model):
    name = models.TextField()
    b_owner = models.ForeignKey(null=True)
    contact = models.CharField(max_length=20)
    email = models.EmailField(max_length=75, null=True)
    description = models.TextField(default='hood business')
    hood = models.ForeignKey(Hood, related_name='business')


class Post(models.Model):
    user = models.ForeignKey(Profile)
    Text = models.TextField(null=True)
    hoodwatch = models.ForeignKey(Hood, related_name='posts')
