from django import forms
from django.forms import Textarea

from .models import UserContact


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
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'


	def clean_contact(self,*args,**kwargs):
		contactNumber = self.cleaned_data.get("contact")
		if len(contactNumber) < 10:
			print("this condition has to be met")
			raise forms.ValidationError("Please enter a valid Mobile Number")
		return contactNumber
