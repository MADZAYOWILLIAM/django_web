from django import forms

from .models import ServiceRequest


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
