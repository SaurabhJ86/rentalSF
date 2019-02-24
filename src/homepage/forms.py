from django import forms
from django.forms import Textarea,TextInput

from .models import UserContact,ListProperty,PropertyListADCreation,UserScheduleVisit


class ContactForm(forms.ModelForm):
	class Meta:
		model = UserContact
		fields = [
			'username',
			'contact'
		]
		widgets = {
			'username': Textarea(attrs={"cols":30,"rows":1,"placeholder":"Your Name"}),
			'contact': Textarea(attrs={"cols":30,"rows":1,"placeholder":"Mobile Number"}),
		}
	def __init__(self,*args,**kwargs):
		super(ContactForm,self).__init__(*args,**kwargs)
		# for visible in self.visible_fields():
		for field in iter(self.fields):
			if field == "contact":
				self.fields[field].widget.attrs.update({"class":"form-control col-sm-3 .offset-sm-3"})
			else:
				self.fields[field].widget.attrs.update({"class":"form-control"})
			# print(visible)
			# visible.field.widget.attrs['class'] = 'form-control'


	def clean_contact(self,*args,**kwargs):
		contactNumber = self.cleaned_data.get("contact")
		if len(contactNumber) < 10:
			raise forms.ValidationError("Please enter a valid Mobile Number")
		return contactNumber


class ListPropertyForm(forms.ModelForm):
	class Meta:
		model 	= ListProperty
		labels 	= {
			'area':"Area in Pune",
			'contact':"Your Contact Number",
			'ownername':'Name',
		} 
		widgets = {
			'property_type': Textarea(attrs={"cols":50,"rows":2,"placeholder":"Flat or Independent House"}),
		}
		exclude = ['timestamp','updated','is_active']

	# Add the bootstrap class "form-control to each of the field of the form."
	def __init__(self,*args,**kwargs):
		super(ListPropertyForm,self).__init__(*args,**kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({"class":"form-control"})

	def clean_contact(self):
		contact = self.cleaned_data.get("contact")
		if len(contact) < 10:
			raise forms.ValidationError("Please enter a valid Mobile Number")
		return contact



class PropertyListADForm(forms.ModelForm):
	class Meta:
		model = PropertyListADCreation
		exclude = ['timestamp','updated']
	def __init__(self,*args,**kwargs):
		super(PropertyListADForm,self).__init__(*args,**kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({"class":"form-control"})		



class ScheduleVisitForm(forms.ModelForm):
	class Meta:
		model = UserScheduleVisit
		fields = ["name","contact","email"]

	def __init__(self,*args,**kwargs):
		super(ScheduleVisitForm,self).__init__(*args,**kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({"class":"form-control"})

