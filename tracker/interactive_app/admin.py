from django.contrib import admin
from interactive_app.models import UserProfile, Organization, City, JobPosting

admin.site.register(UserProfile)
admin.site.register(JobPosting)

class OrganizationAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Organization, OrganizationAdmin)

class CityAdmin(admin.ModelAdmin):
	search_fields = ('city',)

admin.site.register(City, CityAdmin)
