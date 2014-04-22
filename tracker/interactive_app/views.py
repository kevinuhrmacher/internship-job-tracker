from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib import messages
from interactive_app.models import UserProfile, City, Organization
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from interactive_app.forms import ProfileForm

def home(request):
    user_list = UserProfile.objects.all()
    organization_list = Organization.objects.all()
    city_list = City.objects.all()
    return render(request, "interactive_app/home.html", {'users': user_list, 'organizations': organization_list, 'cities': city_list})

def about(request):
    return render(request, 'interactive_app/about.html')
    
def user(request, pk):
	user = get_object_or_404(UserProfile, id=pk)
	return render(request, "interactive_app/user.html", {'user': user})

def userList(request):
	user_list = UserProfile.objects.all()
	paginator = Paginator(user_list, 100)
	page = request.GET.get('page')
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer, deliver first page.
		users=paginator.page(1)
	except EmptyPage:
		#i f page is out of range (eg 9000), deliver last page of results.
		users = paginator.page(paginator.num_pages)
	return render(request, 'interactive_app/user_list.html', {"users":users})

def city(request, pk):
    city = get_object_or_404(City, id=pk)
    current_people = UserProfile.objects.filter(current_city = pk)
    local_orgs = Organization.objects.filter(city = pk)
    return render(request, "interactive_app/city.html", {'city':city, 'current_people': current_people, 'local_orgs': local_orgs})

def cityList(request):
	city_list = City.objects.all()
	paginator = Paginator(city_list, 100)
	page = request.GET.get('page')
	try:
		cities = paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer, deliver first page.
		cities=paginator.page(1)
	except EmptyPage:
		#i f page is out of range (eg 9000), deliver last page of results.
		cities = paginator.page(paginator.num_pages)
	return render(request, "interactive_app/city_list.html", {"cities":cities})

def organization(request,pk):
    organization = get_object_or_404(Organization, id=pk)
    current_people = UserProfile.objects.filter(current_company = pk)

    return render(request, "interactive_app/organization.html", {'organization':organization, 'current_people': current_people})

def organizationList(request):
	organization_list = Organization.objects.all()
	paginator = Paginator(organization_list, 100)
	page = request.GET.get('page')
	try:
		organizations = paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer, deliver first page.
		organizations = paginator.page(1)
	except EmptyPage:
		#i f page is out of range (eg 9000), deliver last page of results.
		organizations = paginator.page(paginator.num_pages)
	return render(request, "interactive_app/organization_list.html", {"organizations":organizations})

def profile_settings(request):
  user_list = UserProfile.objects.all()
  organization_list = Organization.objects.all()
  city_list = City.objects.all()
  if request.method == 'POST':
      form = ProfileForm(request.POST, request.FILES, instance=UserProfile.objects.get(user=request.user))

      if form.is_valid():

          profile = form.save(commit=False)
          profile.save()

          messages.success(request,'updated')
          return render(request, "interactive_app/home.html", {'users': user_list, 'organizations': organization_list, 'cities': city_list})

  else:
      user = request.user

      try:
          profile = getattr(user, 'profile')
      except:
          profile = UserProfile()
          profile.user = user
          profile.save()

      form = ProfileForm(instance=UserProfile.objects.get(user=request.user))

  return render(request, 'interactive_app/settings.html', {'form': form})
