from django import forms
from .models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'subject', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'İsim','class': 'col-lg-6 col-12 form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Konu','class': 'col-lg-6 col-12 form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-posta', 'class': 'col-lg-6 col-12 form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Mesaj','class': 'col-lg-6 col-12 form-control'}),
        }