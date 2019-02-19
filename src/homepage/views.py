from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import PropertyListADCreation,UserContact
from .forms import ContactForm,ListPropertyForm,PropertyListADForm
def homepage(request):

	form = ContactForm(request.POST or None)
	templates = "home.html"

	if form.is_valid():
			form.save()
			form = ContactForm()

	context = {
		"form":form,
	}

	return render(request,templates,context)



class getContact(generic.View):

	def post(self,request,*args,**kwargs):
		# if form.is_valid():
			# username = request.POST.get("name")
			# contact = request.POST.get("number")
			# UserContact.create(username=username,contact=contact)			
		username = request.POST.get("name")
		contact = request.POST.get("number")
		UserContact.objects.create(username=username,contact=contact)

		print(username)
		print(contact)

		return HttpResponse("<h3>We have received your details.One of our team members will contact you shortly.</h3>")



def owner(request):

	templates = "owner.html"

	context = {}

	return render(request,templates,context)


def listProperty(request):

	form = ListPropertyForm(request.POST or None)

	if form.is_valid():
		form.save()
		form = ListPropertyForm()
		# This will return the message to be displayed back to the end user.
		messages.success(request,"Details submitted successfully.Our team will contact you shortly.")

	templates = "listProperty.html"

	context = {
		"form":form
	}

	return render(request,templates,context)


# @login_required
def createListPropertyAD(request):
	is_admin = False

	get_properties = PropertyListADCreation.objects.all()

	# This will make sure that only superuser can create the AD.
	if request.user.is_superuser:
		is_admin = True

	form = PropertyListADForm(request.POST or None)

	if form.is_valid():
		form.save()
		form = PropertyListADForm()

		messages.success(request,"New Property AD has been posted successfully.Please refresh the page to see the AD.")

	templates = "listPropertyAD.html"

	context = {
		"form":form,
		"is_admin": is_admin,
		"properties":get_properties,
	}


	return render(request,templates,context)

