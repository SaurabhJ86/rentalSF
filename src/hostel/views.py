from django.shortcuts import render

from .models import Hostel


def hostelLandingPage(request):

	farmView = Hostel.objects.first()

	templates = 'hostel/hostelLandingPage.html'

	context = {
		"farmView":farmView,
	}


	return render(request,templates,context)
