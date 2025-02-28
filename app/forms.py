from django import forms
from django.forms.widgets import TextInput
from app.models import Wardrobe

class WardrobeForm(forms.ModelForm):
    class Meta:
        model = Wardrobe
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control','placeholder': 'Enter Name'}),
            'type': TextInput(attrs={'class': 'form-control','placeholder': 'Enter Type'}),
            'color': TextInput(attrs={'class': 'form-control','placeholder': 'Enter Color'}),
            'size': TextInput(attrs={'class': 'form-control','placeholder': 'Enter Size'}),
            'season': TextInput(attrs={'class': 'form-control','placeholder': 'Enter Season'}),
            'date': TextInput(attrs={'class': 'form-control','placeholder': 'Enter Date'}),
        }