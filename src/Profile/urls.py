from django.urls import path

from .views import signup

app_name='Profile'

urlpatterns = [
	path('',signup,name='profile-signup'),
]