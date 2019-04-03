from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from .forms import (
		ProfilePreferenceForm,
		SignUpForm,
		UpdateProfileForm,
		UpdateUserForm
	)
from .models import Profile

def signup(request):

	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			next_url = request.GET.get("next","")
			form.save()
			username = form.cleaned_data.get("username")
			raw_password = form.cleaned_data.get("password1")
			user = authenticate(username=username,password=raw_password)
			login(request,user)
			if next_url:
				return redirect(next_url)
			return redirect('listProperty')

	else:
		form = SignUpForm()
	template = 'signup.html'

	context = {
		"form":form
	}

	return render(request,template,context)


@login_required(login_url="login")
def account(request):
	username = request.user
	template = "accounts.html"

	context = {}

	return render(request,template,context)

# This will show the save property.
@login_required(login_url="login")
def saveProperty(request):
	savedProperties = []
	user = User.objects.get(id=request.user.id)
	profile = Profile.objects.get(user=user)
	if profile.saveProperty.all():
		savedProperties = profile.saveProperty.all()


	template = "showSaveProperty.html"

	context = {
	"savedProperties":savedProperties,
	"profile":profile,
	}

	return render(request,template,context)

@login_required(login_url="login")
def updateProfile(request):

	profile_instance = Profile.objects.get(user=request.user)

	if request.method == "POST":
		user_form = UpdateUserForm(request.POST ,instance=request.user)
		profile_form = UpdateProfileForm(request.POST,instance = profile_instance)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
	else:
		user_form = UpdateUserForm(instance=request.user)
		profile_form = UpdateProfileForm(instance=profile_instance)

	template = 'updateProfile.html'

	context = {
		"user_form":user_form,
		"profile_form":profile_form,
	}

	return render(request,template,context)

@login_required(login_url="login")
def preferences(request):

	if request.method == "POST":
		form = ProfilePreferenceForm(request.POST)
		if form.is_valid():
			print("Form is coming")
	else:
		form = ProfilePreferenceForm()
	template = "selectPreference.html"

	context = {
		"form":form
	}


	return render(request,template,context)

