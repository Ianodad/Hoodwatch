from django import forms
from .models import Profile, Hood, Business, Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name",]
