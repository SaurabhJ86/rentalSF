import uuid

from django.db import models

from homepage.utils import resize_image


def farmViewImageUploadPath(instance,filename):
	get_unique_id = uuid.uuid1()
	filename = str(get_unique_id) + filename
	return "farmview/{filename}".format(filename=filename)		


class Hostel(models.Model):

	name 		= models.CharField(max_length=120)
	image 		= models.ImageField(upload_to=farmViewImageUploadPath,null=True,blank=True)
	address 	= models.TextField(null=True,blank=True)
	rooms 		= models.IntegerField()
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	cctv 		= models.BooleanField(default=True)
	kitchen 	= models.BooleanField(default=False)
	parking 	= models.BooleanField(default=False)

	__original_image = None

	def __init__(self,*args,**kwargs):
		super(Hostel,self).__init__(*args,**kwargs)
		self.__original_image = self.image

	def save(self,*args,**kwargs):
		if self.image:
			if self.image == self.__original_image:
				pass
			else:
				resize_image(self.image,[800,400])
		super(Hostel,self).save(*args,**kwargs)

	def __str__(self):
		return self.name