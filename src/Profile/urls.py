from django.urls import path

from .views import account,signup

app_name='Profile'

urlpatterns = [
	path('',signup,name='profile-signup'),
	path('account/',account,name='profile-account'),
]