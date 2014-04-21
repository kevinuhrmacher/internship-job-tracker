from django import forms
from django.forms import ModelForm
from interactive_app.models import UserProfile, City, Organization

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = [
          'skillset',
          'email',
          'bio',
          'graduation_year',
          'major',
          'img_url',
          'portfolio',
          'twitter',
          'current_position',
          'current_city',
          'current_company'
        ]
