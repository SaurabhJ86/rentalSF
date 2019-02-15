from django.contrib import admin

# Register your models here.
from .models import UserContact,RSImages,ListProperty


admin.site.register(UserContact)
admin.site.register(RSImages)
admin.site.register(ListProperty)