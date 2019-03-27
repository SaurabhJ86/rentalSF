from django.contrib.auth import login,authenticate
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


from .forms import SignUpForm


def signup(request):

	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			raw_password = form.cleaned_data.get("password1")
			user = authenticate(username=username,password=raw_password)
			login(request,user)
			return redirect('listProperty')

	else:
		form = SignUpForm()
	template = 'signup.html'

	context = {
		"form":form
	}

	return render(request,template,context)


@login_required(login_url="login")
def account(request):
	username = request.user
	template = "accounts.html"

	context = {}

	return render(request,template,context)