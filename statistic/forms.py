from django import forms
from .models import *

from live.models import *




class CountryDataForm(forms.ModelForm):
    class Meta:
        model = CountryData
        fields = '__all__'



class DateDataForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ('date_creation', 'action')