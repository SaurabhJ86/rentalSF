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


class SavePropertyTracker(models.Model):
	savedProperty 	= models.ForeignKey(PropertyListADCreation,on_delete=models.CASCADE)
	profile 		= models.ForeignKey(Profile,on_delete=models.CASCADE)
	timestamp 		= models.DateTimeField(auto_now=True)
	updated 		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		self.profile.user.username

class ProfilePreference(models.Model):

	profile 				= models.ForeignKey(Profile,on_delete=models.CASCADE)
	school					= models.BooleanField(default=False)
	market					= models.BooleanField(default=False)
	hospital				= models.BooleanField(default=False)
	location				= models.CharField(max_length=120)
	distance_from_location 	= models.IntegerField()
	price_start_range 		= models.CharField(max_length=5)
	price_end_range 		= models.CharField(max_length=5)


	def __str__(self):
		return self.profile.user.username


@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)



@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
	instance.profile.save()
