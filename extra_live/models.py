from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class ClientExtra(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class TypeExtra(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class CompetitionExtra(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class TeamsExtra(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class TacheExtraLive(models.Model):
    STATUS_CHOICES = (
        ('creer', 'CREER'),
        ('a_creer', 'A_CREER'),       
    )
        

    client = models.ForeignKey(ClientExtra, on_delete=models.CASCADE)
    type =  models.ForeignKey(TypeExtra, on_delete=models.CASCADE)
    competition =  models.ForeignKey(CompetitionExtra, on_delete=models.CASCADE)
    evenement = models.CharField(max_length=255)
    titre = models.CharField(max_length=255)
    date_creation = models.DateTimeField()
    teams = models.ForeignKey(TeamsExtra, on_delete=models.CASCADE)
    action = models.CharField(choices=STATUS_CHOICES, default='a_creer', max_length=10)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('extra_live:extra_detail', kwargs={'pk': self.pk})
    
    def get_absolute_url_update(self):
        return reverse('extra_live:extra_modify', kwargs={'pk': self.pk})

