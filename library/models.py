from django.db import models
from django import forms

class UserProfile(models.Model):
    bio = models.CharField(max_length=300)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    contact_info = models.CharField(max_length=100)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'contact_info']
