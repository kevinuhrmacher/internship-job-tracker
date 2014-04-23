from django.contrib.auth.models import User
from django.db import models
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount

import hashlib


class City(models.Model):
    name = models.TextField(null=True)
    state = models.TextField(null=True)
    lat = models.TextField(null=True)
    longitude = models.TextField(null=True)
    img_url = models.TextField(null = True)
    class Meta(object):
        verbose_name_plural = "cities"
        ordering = ('name',)
    def __unicode__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.name=self.name.upper()
        super(City, self).save(*args, **kwargs)

class Organization(models.Model):
    name = models.TextField(null=True)
    url = models.TextField(null=True)
    bio = models.TextField(null=True)
    contact = models.TextField(null=True)
    city = models.ForeignKey(City)
    opening = models.TextField(null=True)
    twitter = models.TextField(null=True)
    img_url = models.TextField(null=True)
    address = models.TextField(null=True)
    lat = models.TextField(null=True)
    longitude = models.TextField(null=True)
    class Meta(object):
        verbose_name_plural = "organizations"
        ordering = ('name',)
    def __unicode__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.name=self.name.upper()
        super(Organization, self).save(*args, **kwargs)

class UserProfile(models.Model):
    SKILLSET_CHOICES = (
      ('Design', 'Designer'),
      ('Coder', 'Programmer'),
      ('Photo', 'Photographer'),
      ('Reporting', 'Reporter'),
      ('Other', 'Other'),
    )

    user = models.OneToOneField(User, related_name='profile')
    skillset = models.CharField(max_length=10,choices=SKILLSET_CHOICES)
    email = models.TextField(null=True, blank=True)
    graduation_year = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    major = models.TextField(null=True, blank=True)
    img_url = models.TextField(null=True, default = 'http://www.dotnetcodesg.com/Register/UserImage/Default.png')
    portfolio = models.TextField(null=True, blank=True)
    twitter = models.TextField(null=True, blank=True)
    current_position = models.TextField(null=True, blank=True)
    current_city = models.ForeignKey(City, null=True, blank=True)
    current_company = models.ForeignKey(Organization, null=True, blank=True)

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    class Meta:
        db_table = 'user_profile'

    def profile_image_url(self):
        """
        Return the URL for the user's Facebook icon if the user is logged in via Facebook,
        otherwise return the user's Gravatar URL
        """
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')

        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)

        return "http://www.dotnetcodesg.com/Register/UserImage/Default.png".format(
            hashlib.md5(self.user.email).hexdigest())

    def account_verified(self):
        """
        If the user is logged in and has verified hisser email address, return True,
        otherwise return False
        """
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class JobPosting(models.Model):
    JOBTYPE_CHOICES = (
    ("Internship","Internship"),
    ("Job","Job")
    )

    title = models.CharField(max_length = 100, null=True)
    jobType = models.CharField(max_length=10,choices=JOBTYPE_CHOICES)
    link = models.CharField(max_length = 50, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True)
    contact = models.CharField(max_length = 50, null=True, blank=True)
    timeFrame = models.DateTimeField(null=True, blank=True)
    organization = models.ForeignKey(Organization, null=True, blank=True)


class Position(models.Model):
    department = models.TextField(null=True)
    skillset = models.TextField(null=True)
