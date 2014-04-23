from django import forms
from django.forms import ModelForm
from interactive_app.models import UserProfile, City, Organization, JobPosting

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

class JobForm(forms.Form):
  JOBTYPE_CHOICES = (
  ("Internship","Internship"),
  ("Job","Job")
  )

  title = forms.CharField(widget=forms.TextInput(), max_length=100)
  jobType = forms.ChoiceField(choices=JOBTYPE_CHOICES)
  link = forms.CharField(widget=forms.TextInput(), max_length=100)
  desc = forms.CharField(widget=forms.Textarea())
  timeFrame = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'mm/dd/yyy'}))
  contact = forms.CharField(widget=forms.TextInput(), max_length=100)
  organization = forms.ModelChoiceField(queryset=Organization.objects.all())

# class JobForm(ModelForm):
#   class Meta:
#       model = JobPosting
