from django import forms
from .models import Contact
    
class FormName(forms.Form):
    Name = forms.CharField(label="name", max_length=100)
    Email = forms.EmailField(label="email", max_length=100)
    message = forms.CharField(label="text", max_length=100)
    

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']