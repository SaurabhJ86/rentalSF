from django.contrib import admin

# Register your models here.
from .forms import PropertyListRoomForm
from .models import (
		ImagesPropertyListing,
		ListProperty,
		PropertyListADCreation,
		PropertyListRooms,
		RSImages,
		RSImagesMain,
		UserContact,
		UserScheduleVisit,
	)

class PropertyListRoomAdmin(admin.ModelAdmin):

	form = PropertyListRoomForm


admin.site.register(UserContact)
admin.site.register(RSImages)
admin.site.register(ListProperty)
admin.site.register(PropertyListADCreation)
admin.site.register(UserScheduleVisit)
admin.site.register(RSImagesMain)
admin.site.register(ImagesPropertyListing)
admin.site.register(PropertyListRooms,PropertyListRoomAdmin)