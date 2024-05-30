from django.forms import ModelForm
from .models import Tache
from django import forms


class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['client', 'type', 'competition', 'evenement', 'titre', 'date_creation', 'action', 'author']


        widgets = {
            'client': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'competition': forms.TextInput(attrs={'class': 'form-control'}),
            'evenement': forms.TextInput(attrs={'class': 'form-control'}),
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'action': forms.Select(attrs={"name": "select_0","class": "form-control"})


    }
        
        
        

    date_creation = forms.DateTimeField(
        input_formats = ['%Y-%m-%dT  %H:%M'],
        widget = forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'},
            format='%Y-%m-%dT  %H:%M')
    )


    # action = forms.BooleanField(
    #     required=False,
    #     label='Action   ',
    #     widget=forms.CheckboxInput)