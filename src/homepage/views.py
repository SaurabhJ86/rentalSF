from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.shortcuts import redirect,render,get_object_or_404
from django.views import generic
from django.views.generic import View

# Create your views here.
from .models import PropertyListADCreation,UserContact,RSImages
from .forms import ContactForm,ListPropertyForm,PropertyListADForm,ScheduleVisitForm,UserScheduleVisit

from Profile.models import Profile
def homepage(request):
	images = RSImages.objects.all()
	form = ContactForm(request.POST or None)
	templates = "home.html"

	if form.is_valid():
			try:
				form.save()
				form = ContactForm()
				messages.success(request,"Details submitted successfully.Our team will contact you shortly.")
			except:
				messages.error(request,"Something went wrong. Please try later.")
				form = ContactForm()

	context = {
		"form":form,
		"images":images,
	}

	return render(request,templates,context)



class getContact(generic.View):

	def post(self,request,*args,**kwargs):			
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

	get_room_type = request.GET.get("q")
	if get_room_type:
		# You can add more filters as you go on.
		# get_properties = get_properties.filter(room_type=get_room_type,is_active=True)
		get_properties = get_properties.filter(room_type=get_room_type).filter(is_active=True)

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


def showProperty(request,id):
	profile = None
	property_saved = False

	if request.user.is_authenticated:
		if not request.user.is_superuser:
			profile = request.user.profile

	visit = request.POST.get("visit")
	get_object = get_object_or_404(PropertyListADCreation,id=id)

	if profile:
		property_saved = profile.check_property(get_object)

	visitForm = ScheduleVisitForm(request.POST or None)

	update_message = ""

	if visit == "true":
		username = request.POST.get("name")
		contact  = request.POST.get("contact")
		email 	 = request.POST.get("email")

		try:
			new_contact = "+91" + contact[-10:]
			UserScheduleVisit.objects.create(name=username,contact=new_contact,email=email)
			update_message = "Received_Contact_Details"
		except Exception as e:
			update_message = "Error_Received"	

		return HttpResponse(update_message)


	template = "showProperty.html"

	context = {
		"get_object":get_object,
		"visitForm":visitForm,
		"property_saved":property_saved,
		"profile":profile,
	}


	return render(request,template,context)

"""
This CBV will interact with the Manager method to toggle the user from the property.
Since this View would be used by both showSaveProperty.html and showProperty.html, and both have different way to handle this
such as showProperty.html which uses Ajax whereas showSaveProperty.html uses the form, therefore I have put this filter "form"
to check whether the call is coming from Ajax or from a Form.
"""
class PropertyToggle(View):
	def post(self,request,*args,**kwargs):
		property_to_toggle 	= request.POST.get("property")
		profile 			= request.POST.get("profile")
		form 				= request.POST.get("form")
		_profile,status 	= Profile.objects.toggle_property(profile,property_to_toggle)
		if form:
			return redirect('Profile:profile-saveproperty')
		return HttpResponse(status)


