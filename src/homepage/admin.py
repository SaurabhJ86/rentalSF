from django.contrib import admin

# Register your models here.
from .models import UserContact,RSImages,ListProperty,PropertyListADCreation,UserScheduleVisit


admin.site.register(UserContact)
admin.site.register(RSImages)
admin.site.register(ListProperty)
admin.site.register(PropertyListADCreation)
admin.site.register(UserScheduleVisit)