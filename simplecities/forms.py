
from django import forms
from simplecities.models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location



