from django import forms

# from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.shortcuts import render,redirect
from .models import Profile,ProfilePreference


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30,required=False,help_text='Optional')
	last_name = forms.CharField(max_length=30,required=False,help_text='Optional')
	email = forms.EmailField(max_length=254,help_text='Required. Inform a valid email address')


	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password1','password2']



class UpdateProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['phone']


class UpdateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']



class ProfilePreferenceForm(forms.ModelForm):

	class Meta:
		model = ProfilePreference
		fields = ["location","distance_from_location","school","market","hospital"]
		labels 	= {
			"location": "Search for Location",
		}
		help_texts = {
			'location': "For Pune only.",
		}

	def __init__(self,*args,**kwargs):
		super(ProfilePreferenceForm,self).__init__(*args,**kwargs)
		self.fields['location'].widget.attrs['id'] 						= 'enterLocation'
		