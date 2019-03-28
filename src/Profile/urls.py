from django.urls import path

from .views import account,saveProperty,signup,updateProfile

app_name='Profile'

urlpatterns = [
	path('',signup,name='profile-signup'),
	path('account/',account,name='profile-account'),
	path('saveproperty/',saveProperty,name='profile-saveproperty'),
	path('update/',updateProfile,name='profile-update'),
]