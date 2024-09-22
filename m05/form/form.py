from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'contact_Name': forms.TextInput(attrs={
                'class': 'form-input w-full rounded mb-4'
            }),
            'contact_Date': forms.SelectDateWidget(attrs={
                'class': 'w-1/3 rounded mb-4'
                }),
            'contact_Email': forms.TextInput(attrs={
                'class': 'form-input w-full rounded mb-4'
            }), 
            'contact_Message': forms.Textarea(attrs={
                'class': 'textarea w-full rounded bg-slate-200 mb-4'
                }),
        }
