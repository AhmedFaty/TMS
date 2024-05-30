from django.db import models

# Create your models here.
from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class ClientHl(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class TypeHl(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class CompetitionHl(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class TeamsHl(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class TacheHlive(models.Model):
    STATUS_CHOICES = (
        ('creer', 'CREER'),
        ('a_creer', 'A_CREER'),       
    )
        

    client = models.ForeignKey(ClientHl, on_delete=models.CASCADE)
    type =  models.ForeignKey(TypeHl, on_delete=models.CASCADE)
    competition =  models.ForeignKey(CompetitionHl, on_delete=models.CASCADE)
    evenement = models.CharField(max_length=255)
    titre = models.CharField(max_length=255)
    date_creation = models.DateTimeField()
    teams = models.ForeignKey(TeamsHl, on_delete=models.CASCADE)
    action = models.CharField(choices=STATUS_CHOICES, default='a_creer', max_length=10)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('hight_live:hl_detail', kwargs={'pk': self.pk})
    
    def get_absolute_url_update(self):
        return reverse('hight_live:hl_modify', kwargs={'pk': self.pk})
