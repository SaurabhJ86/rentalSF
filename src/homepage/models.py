import datetime
import re
import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

# from phonenumber_field.modelfields import PhoneNumberField

from PIL import Image
from resizeimage import resizeimage
from django.core.files.base import ContentFile
from io import BytesIO

from .utils import resize_image

def upload_image(instance,filename):
	get_unique_id = uuid.uuid1()
	filename = str(get_unique_id) + filename	
	return "community/{filename}".format(filename=filename)

def main_upload_image(instance,filename):
	get_unique_id = uuid.uuid1()
	filename = str(get_unique_id) + filename
	return "main_img/{filename}".format(filename=filename)

def list_Property_images(instance,filename):
	get_unique_id = uuid.uuid1()
	filename = str(get_unique_id) + filename
	return "property_images/{filename}".format(filename=filename)	

"""
This will make sure that image being uploaded to S3 has a unique filename otherwise it will replace the existing
image with the same name.
"""
def upload_prop_image(instance,filename):
	get_unique_id = uuid.uuid1()
	filename = str(get_unique_id) + filename
	return "prop/{filename}".format(filename=filename)

class UserContact(models.Model):
	username 		= models.CharField(max_length=120)
	contact 		= models.CharField(max_length=14)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	resolved 		= models.BooleanField(default=False)	

	def __str__(self):
		return self.username


"""
This will display the images on the home page.
"""
class RSImages(models.Model):
	name 			= models.CharField(max_length=120,null=True,blank=True)
	content 		= models.TextField(null=True,blank=True)
	image 			= models.ImageField(upload_to=upload_image,null=True,blank=True)

	class Meta:
		verbose_name = "Image"
		verbose_name_plural = "Images"

	__original_image = None
	
	def __init__(self,*args,**kwargs):
		super(RSImages,self).__init__(*args,**kwargs)
		self.__original_image = self.image
	
	def save(self,*args,**kwargs):
		if self.image:
			if self.image == self.__original_image:
				pass
			else:

				resize_image(self.image,[275,200])

		super(RSImages,self).save(*args,**kwargs)			

	def __str__(self):
		return self.name

"""
This will display the bigger images of the image above created on the Bootstrap modal.
"""
class RSImagesMain(models.Model):
	image_ID 	= models.ForeignKey(RSImages,on_delete=models.CASCADE)
	image 		= models.ImageField(upload_to=main_upload_image,null=True,blank=True)
	image_name 	= models.CharField(max_length=120,null=True,blank=True)
	timestamp 	= models.DateTimeField(auto_now=True)
	updated 	= models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name 		= "Home Enlarged Image"
		verbose_name_plural = "Home Enlarged Images"

	def __str__(self):
		return self.image_name

	__original_image = None
	def __init__(self,*args,**kwargs):
		super(RSImagesMain,self).__init__(*args,**kwargs)
		__original_image = self.image

	def save(self,*args,**kwargs):
		if self.image:
			if self.image == self.__original_image:
				pass
			else:
				resize_image(self.image,[600,500])

		super(RSImagesMain,self).save(*args,**kwargs)

"""
This model would be used by the owner to list their property.
"""
class ListProperty(models.Model):
	ownername 		= models.CharField(max_length=120)
	property_type 	= models.CharField(max_length=120)
	area 			= models.CharField(max_length=120)
	phone_regex 	= RegexValidator(regex=re.compile("(0/91)?[7-9][0-9]{9}"),message="Please enter a valid number.")
	contact 		= models.CharField(validators = [phone_regex],max_length=120)
	email 			= models.EmailField(blank=True,null=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	is_active 		= models.BooleanField(default=False)

	def __str__(self):
		return self.ownername

"""
This model is used to create the Property Listing AD's.
"""
class PropertyListADCreation(models.Model):
	property_type 	= models.CharField(max_length=120)
	about_property 	= models.TextField()
	rent 			= models.CharField(max_length=25)
	deposit 		= models.CharField(max_length=40)
	area 			= models.CharField(max_length=120)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	available_on 	= models.DateField(null=True,blank=True)
	address 		= models.CharField(max_length=150,null=True,blank=True)
	is_active 		= models.BooleanField(default=False)
	property_image 	= models.ImageField(upload_to=upload_prop_image,null=True,blank=True)
	gender 			= models.CharField(max_length=30,default="Boys/Girls/Family")
	furnished 		= models.CharField(max_length=30,default="Fully Furnished")
	features 		= models.TextField(null=True,blank=True)
	offer 			= models.BooleanField(default=False)
	offers 			= models.TextField(null=True,blank=True)
	bed_available 	= models.IntegerField(default=1)
	room_type 		= models.CharField(max_length=40,default="shared")
	extra_charges 	= models.CharField(max_length=4,default="2000")
	total_rooms 	= models.IntegerField(default=1)
	bathrooms 		= models.IntegerField(default=1)

	__original_image = None

	"""
	1.This will hold the original image name, so that we can compare if the property_image has been changed.
	"""
	def __init__(self,*args,**kwargs):
		super(PropertyListADCreation,self).__init__(*args,**kwargs)
		self.__original_image = self.property_image

	# Resize the image to a particular size.
	def save(self,*args,**kwargs):
		if self.property_image:
			# 2.If there is no change in Step 1, then we will pass, otherwise we will upload the new image.
			# This way it allows you to save the upload bandwidth.
			if self.property_image == self.__original_image:
				pass
			else:
				pil_image_obj 	= Image.open(self.property_image)
				resize_image(self.property_image,[400,300])

		super(PropertyListADCreation,self).save(*args,**kwargs)

	def get_absolute_url(self,**kwargs):
			return reverse("showProperty",kwargs={"id":self.id})

	def get_features(self):
		if self.features:
			return self.features.split("\n")

	def get_offers(self):
		if self.offers:
			return self.offers.split("\n")
	# This method will check whether to show Now or the available_on date.
	def valid_date(self):
		if self.available_on:
			get_current_data = datetime.datetime.now().date()
			if self.available_on > get_current_data:
				return True
			return False

	def __str__(self):
		return self.property_type

# This model will be used to create rooms for each Property Listed above.
class PropertyListRooms(models.Model):

	prop 			= models.ForeignKey(PropertyListADCreation,on_delete=models.CASCADE)
	# Use something like, Room 1,Room 2.
	name 			= models.CharField(max_length=25,null=True,blank=True)
	is_available 	= models.BooleanField(default=True)
	bed_available 	= models.IntegerField(default=1)
	private_room	= models.BooleanField(default=False)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	deposit 		= models.CharField(max_length=40)
	rent 			= models.CharField(max_length=40)

	class Meta:
		verbose_name_plural = "Property List Room"


	def __str__(self):
		return self.prop.property_type + " " +  str(self.name)


"""
This model class will be used to create multiple images for the model PropertyListADCreation.
"""
class ImagesPropertyListing(models.Model):
	image_for 		= models.ForeignKey(PropertyListADCreation,on_delete=models.CASCADE,limit_choices_to={"rent":7000})
	image 			= models.ImageField(upload_to=list_Property_images,null=True,blank=True)
	image_content 	= models.CharField(max_length=200,null=True,blank=True)
	timestamp 		= models.DateTimeField(auto_now=True)
	updated 		= models.DateTimeField(auto_now_add=True)

	__original_image = None

	def __init__(self,*args,**kwargs):
		super(ImagesPropertyListing,self).__init__(*args,**kwargs)
		self.__original_image = self.image


	def save(self,*args,**kwargs):
		if self.__original_image == self.image:
			pass
		else:
			pil_image_obj = Image.open(self.image)
			resize_image(self.image,[400,300])
		super(ImagesPropertyListing,self).save(*args,**kwargs)

	def __str__(self):
		return self.image_content

"""
This model would be used to hold the user details when he/she schedules a visit.
"""
class UserScheduleVisit(models.Model):
	name 			= models.CharField(max_length=120)
	contact 		= models.CharField(max_length=35,null=True,blank=True)
	email 			= models.EmailField()
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name




