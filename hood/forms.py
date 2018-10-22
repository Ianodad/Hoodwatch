from django import forms
from .models import Profile, Hood, Business, Post


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "prof_pic", "bio", "email"]


class Hoodform(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ["name", "image", "description", "occupants_count"]


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ["name", "b_owner", "contac", "email", "description"]
