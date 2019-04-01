from django.contrib import admin

from .models import (
	Profile,
	ProfilePreference,
	SavePropertyTracker
	)

admin.site.register(Profile)
admin.site.register(ProfilePreference)
admin.site.register(SavePropertyTracker)
