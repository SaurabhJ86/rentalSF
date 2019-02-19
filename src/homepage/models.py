from django.db import models
from django.utils import timezone

# Create your models here.

def upload_image(instance,filename):
	return "updates/{filename}".format(filename=filename)

def upload_prop_image(instance,filename):
	return "prop/{filename}".format(filename=filename)

class UserContact(models.Model):
	username 		= models.CharField(max_length=120)
	contact 		= models.CharField(max_length=14)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	resolved 		= models.BooleanField(default=False)


	def __str__(self):
		return self.username



class RSImages(models.Model):
	name 			= models.CharField(max_length=120,null=True,blank=True)
	content 		= models.TextField(null=True,blank=True)
	image 			= models.ImageField(upload_to=upload_image,null=True,blank=True)

	class Meta:
		verbose_name = "Image"
		verbose_name_plural = "Images"

	def __str__(self):
		return self.name


class ListProperty(models.Model):
	ownername 		= models.CharField(max_length=120)
	property_type 	= models.CharField(max_length=120)
	area 			= models.CharField(max_length=120)
	contact 		= models.CharField(max_length=120)
	email 			= models.EmailField(blank=True,null=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	is_active 		= models.BooleanField(default=False)

	def __str__(self):
		return self.ownername


class PropertyListADCreation(models.Model):
	property_type 	= models.CharField(max_length=120)
	about_property 	= models.TextField()
	rent 			= models.CharField(max_length=25)
	deposit 		= models.CharField(max_length=10)
	area 			= models.CharField(max_length=120)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	is_active 		= models.BooleanField(default=False)
	property_image 	= models.ImageField(upload_to=upload_prop_image,null=True,blank=True)
	gender 			= models.CharField(max_length=30,default="Boys/Girls/Family")
	furnished 		= models.CharField(max_length=30,default="Fully Furnished")
	bed_available 	= models.IntegerField(default=1)

	def save(self,*args,**kwargs):
		super(PropertyListADCreation,self).save(*args,**kwargs)

	def __str__(self):
		return self.property_type






