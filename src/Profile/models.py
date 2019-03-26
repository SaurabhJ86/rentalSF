from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from homepage.models import PropertyListADCreation

class ProfileManager(models.Manager):
	def toggle_property(self,profile,toggle_property):
		get_property = PropertyListADCreation.objects.get(id=toggle_property)
		profile = Profile.objects.get(id=profile)
		status = False
		if get_property in profile.saveProperty.all():
			get_property.under_property.remove(profile) 
		else:
			get_property.under_property.add(profile) 
			status = True
		return profile,status


class Profile(models.Model):
	user 			= models.OneToOneField(User,on_delete=models.CASCADE)
	timestamp 		= models.DateTimeField(auto_now=True)
	updated 		= models.DateTimeField(auto_now_add=True)
	phone 			= models.CharField(max_length=20)
	saveProperty 	= models.ManyToManyField(PropertyListADCreation,related_name='under_property',blank=True)

	objects = ProfileManager()

	def check_property(self,save_property):
		if save_property in self.saveProperty.all():
			return True
		return False

	def __str__(self):
		return self.user.username



@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)



@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
	instance.profile.save()
