from django.http import HttpResponse

from django.shortcuts import render
from django.views import generic

# Create your views here.
def homepage(request):


	templates = "home.html"

	context = {}

	return render(request,templates,context)



class getContact(generic.View):

	def post(self,request,*args,**kwargs):
		username = request.POST.get("name")
		contact = request.POST.get("number")

		print(username)
		print(contact)

		return HttpResponse("<h3>We have received your details.One of our team members will contact you shortly.</h3>")