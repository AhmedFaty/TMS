from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Tache(models.Model):
    STATUS_CHOICES = (
        ('creer', 'CREER'),
        ('a_creer', 'A_CREER'),       
    )
    client = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    competition = models.CharField(max_length=255)
    evenement = models.CharField(max_length=255)
    titre = models.CharField(max_length=255)
    date_creation = models.DateTimeField()
    action = models.CharField(choices=STATUS_CHOICES, default='a_creer', max_length=10)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted')

    def get_absolute_url(self):
        return reverse('tache:tache_detail', kwargs={'pk': self.pk})
    
    def get_absolute_url_update(self):
        return reverse('tache:tache_modify', kwargs={'pk': self.pk})

    # def get_absolute_url_delete(self):
    #     return reverse('tache:tache_delete', kwargs={'pk': self.pk})
