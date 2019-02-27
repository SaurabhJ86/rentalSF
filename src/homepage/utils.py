import uuid

from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image
from resizeimage import resizeimage


# def resize_image(image,resize_method,measurements=[]):
def resize_image(image,measurements=[]):

	image_obj = Image.open(image)
	new_image = resizeimage.resize_cover(image_obj,measurements)


	new_image_io = BytesIO()
	new_image.save(new_image_io,format="JPEG")

	temp_name = image.name

	image.save(
		temp_name,
		content = ContentFile(new_image_io.getvalue()),
		save=False
	)
	return image




