from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField
import datetime


# Create your models here.


class Hood(models.Model):
    name = models.TextField()
    image = ImageField(
        manual_crop='1280x720')
    admin = models.ForeignKey("Profile", related_name='hoods')
    description = models.TextField(default='Random group')
    datecreated = models.DateField(_("Date"), default=datetime.date.today)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(default="Anonymous")
    prof_pic = ImageField(
        manual_crop='200x200')
    bio = models.TextField(default="Welcome to the hood")
    hoodwatch = models.ForeignKey(
        hood, blank=True, null=True, related_name='people')

    def __str__(self):
        return f'Profile {self.user.Name}'

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
    b_owner = models.ForeignKey(Profile)
    contact = models.CharField(max_length=20)
    description = models.TextField(default='hood business')
    hood = models.ForeignKey(Hood, related_name='business')


class Post(models.Model):
    user = models.ForeignKey(Profile)
    Text = models.TextField()
    hoodwatch = models.ForeignKey(Hood, related_name='posts')
