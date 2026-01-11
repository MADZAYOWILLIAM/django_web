from django import forms
from .models import Program

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['title', 'description','coordinator', 'start_date', 'end_date', 'capacity', 'image']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
