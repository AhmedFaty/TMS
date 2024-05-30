from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render,  get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import *
from .models import Tache
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.db.models import Count
from collections import Counter
from django.db.models.functions import TruncMonth
import json
from django.db.models.functions import ExtractMonth

from django.contrib.auth.decorators import login_required







class TacheListLiveView(ListView):
    model = Tache
    template_name = 'live/tache_list.html'
    context_object_name = 'taches'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Compter le nombre de tâches actives
        context['bloque'] = Tache.objects.filter(action='a_creer').count()
        # Compter le nombre de tâches bloquées
        context['actifs'] = Tache.objects.filter(action='creer').count()
        return context


    def get_queryset(self) -> QuerySet[Any]:
        return Tache.objects.all().order_by('date_creation')
    


class TacheDetailView(DetailView):
    model = Tache
    # loolup_field = 'id'
    template_name = 'live/tache_detail.html'
    context_object_name = 'taches'


class TacheModifyViews(UpdateView):
    # form_class = TacheForm
    model = Tache
    template_name = 'live/tache_modify.html'
    fields = ('client', 'type', 'competition', 'evenement', 'titre', 'date_creation', 'action')
    
    def get_success_url(self) -> str:
        return reverse('live:tache_detail', kwargs={'pk': self.object.pk})
    

class TacheDeleteViews(DeleteView):
    model = Tache
    success_url = "/live/"
    template_name = 'live/tache_delete.html'



@login_required
def create_campagnes_view(request):

    user_connecte = request.user

    user_connecte = request.user
    form = TacheForm(request.POST or None, user=user_connecte)
    message = ''
    if form.is_valid():
        form.save()
        message = 'Campagne LIVE enregistrer avec success'
        form = TacheForm()
    context = {
        'form': form,
        'message': message,

        }

    return render(request, "live/campagne.html", context)



def tache_live_view(request):
    # Récupérer les mois et compter le nombre de tâches créées pour chaque mois
    taches_per_month = Tache.objects.annotate(month=TruncMonth('date_creation')).values('month').annotate(count=Count('id'))
    # Préparer les données pour le graphique
    months = [tache['month'].strftime('%B-%Y') for tache in taches_per_month]
   
    dates = Tache.objects.values_list('date_creation', flat=True)
    mois = [date.strftime('%B-%Y') for date in dates]
    # Compter le nombre de tâches par mois
    counts = Counter(mois)

    bloque = Tache.objects.filter(action='a_creer').count()
    actifs = Tache.objects.filter(action='creer').count()
    tahe = Tache.objects.all().count()

    

    # Filtrer par client
    form = ClientFilterForm(request.GET)
    clients = ClientLive.objects.all()

    if form.is_valid():
        client_id = form.cleaned_data['client']
        if client_id:
            clients = clients.filter(id=client_id)


    context = {
        'actifs': actifs,
        'bloque': bloque,
        'tahe': tahe,

        'months': json.dumps(months),
        'counts': json.dumps(counts),

        'form': form, 
        'clients': clients


        
        }

    return render(request, 'live/stat.html', context)
