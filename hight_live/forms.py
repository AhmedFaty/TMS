from django.forms import ModelForm
from .models import TacheHlive
from django import forms


class TacheForm(forms.ModelForm):
    class Meta:
        model = TacheHlive
        fields = ['client', 'type', 'competition', 'evenement', 'titre', 'date_creation', 'teams', 'action', 'author']


        widgets = {
            'client': forms.Select(attrs={"name": "select_0","class": "form-control"}),
            'type': forms.Select(attrs={"name": "select_0","class": "form-control"}),
            'competition': forms.Select(attrs={"name": "select_0","class": "form-control"}),
            'evenement': forms.TextInput(attrs={'class': 'form-control'}),
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'teams': forms.Select(attrs={"name": "select_0","class": "form-control"}),
            'action': forms.Select(attrs={"name": "select_0","class": "form-control"}),
            'author': forms.HiddenInput(),  # Champ caché pour l'auteur


    }
        

    def __init__(self, *args, **kwargs):
        # Récupérer l'utilisateur connecté
        user = kwargs.pop('user', None)
        super(TacheForm, self).__init__(*args, **kwargs)
        # Pré-remplir le champ "author" avec l'utilisateur connecté
        if user:
            self.initial['author'] = user
        
        
        
        
        

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