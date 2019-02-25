import uuid

from django.db import models
from django.urls import reverse
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField

from sorl.thumbnail import get_thumbnail,ImageField

from PIL import Image
from resizeimage import resizeimage
from django.core.files.base import ContentFile
from io import BytesIO
# Create your models here.

def upload_image(instance,filename):
	return "updates/{filename}".format(filename=filename)

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
	deposit 		= models.CharField(max_length=40)
	area 			= models.CharField(max_length=120)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	is_active 		= models.BooleanField(default=False)
	# property_image 	= models.ImageField(upload_to=upload_prop_image,null=True,blank=True)
	property_image 	= ImageField(upload_to=upload_prop_image,null=True,blank=True)
	gender 			= models.CharField(max_length=30,default="Boys/Girls/Family")
	furnished 		= models.CharField(max_length=30,default="Fully Furnished")
	bed_available 	= models.IntegerField(default=1)
	room_type 		= models.CharField(max_length=40,default="Shared Room")

	# Resize the image to size.
	def save(self,*args,**kwargs):
		if self.property_image:
			pil_image_obj 	= Image.open(self.property_image)
			new_image 		= resizeimage.resize_cover(pil_image_obj,[400,300])

			new_image_io 	= BytesIO()
			new_image.save(new_image_io,format="JPEG")

			temp_name 		= self.property_image.name

			self.property_image.save(
				temp_name,
				content 	= ContentFile(new_image_io.getvalue()),
				save 		= False
			)
		super(PropertyListADCreation,self).save(*args,**kwargs)

	def get_absolute_url(self,**kwargs):
			return reverse("showProperty",kwargs={"id":self.id})

	def __str__(self):
		return self.property_type


class UserScheduleVisit(models.Model):
	name 			= models.CharField(max_length=120)
	contact 		= PhoneNumberField()
	email 			= models.EmailField()
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name




