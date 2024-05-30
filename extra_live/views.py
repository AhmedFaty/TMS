from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render,  get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import TacheForm
from .models import TacheExtraLive
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.db.models import Count
from collections import Counter
from django.db.models.functions import TruncMonth
import json
from django.db.models.functions import ExtractMonth
from django.contrib.auth.decorators import login_required




# Create your views here.
class TacheListView(ListView):
    model = TacheExtraLive
    template_name = 'extra_live/tache_list_extra.html'
    context_object_name = 'taches'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Compter le nombre de tâches actives
        context['bloque'] = TacheExtraLive.objects.filter(action='a_creer').count()
        # Compter le nombre de tâches bloquées
        context['actifs'] = TacheExtraLive.objects.filter(action='creer').count()
        return context


    def get_queryset(self) -> QuerySet[Any]:
        return TacheExtraLive.objects.all().order_by('date_creation')
    



class TacheDetailExtraView(DetailView):
    model = TacheExtraLive
    # loolup_field = 'id'
    template_name = 'extra_live/tache_detail_extra.html'
    context_object_name = 'taches'


class TacheModifyExtraViews(UpdateView):
    # form_class = TacheForm
    model = TacheExtraLive
    template_name = 'extra_live/tache_modify_extra.html'
    fields = ('client', 'type', 'competition', 'evenement', 'titre', 'teams', 'date_creation', 'action')
    
    def get_success_url(self) -> str:
        return reverse('extra_live:extra_detail', kwargs={'pk': self.object.pk})
    

class TacheDeleteExtraViews(DeleteView):
    model = TacheExtraLive
    success_url = "/extra_live/"
    template_name = 'extra_live/tache_delete_extra.html'


@login_required
def create_campagnes_extra_view(request):

    user_connecte = request.user

    user_connecte = request.user
    form = TacheForm(request.POST or None, user=user_connecte)

    message = ''
    if form.is_valid():
        form.save()
        message = 'Campagne enregistrer avec success'
        form = TacheForm()
    context = {
        'form': form,
        'message': message
        }

    return render(request, "extra_live/campagne_extra.html", context)



def tache_extra_view(request):
    # Récupérer les mois et compter le nombre de tâches créées pour chaque mois
    taches_per_month = TacheExtraLive.objects.annotate(month=TruncMonth('date_creation')).values('month').annotate(count=Count('id'))
    # Préparer les données pour le graphique
    months = [tache['month'].strftime('%B-%Y') for tache in taches_per_month]
   
    dates = TacheExtraLive.objects.values_list('date_creation', flat=True)
    mois = [date.strftime('%B-%Y') for date in dates]
    # Compter le nombre de tâches par mois
    counts = Counter(mois)

    bloque = TacheExtraLive.objects.filter(action='a_creer').count()
    actifs = TacheExtraLive.objects.filter(action='creer').count()
    tahe = TacheExtraLive.objects.all().count()



    context = {
        'actifs': actifs,
        'bloque': bloque,
        'tahe': tahe,

        'months': json.dumps(months),
        'counts': json.dumps(counts),


        
        }

    return render(request, 'extra_live/stat.html', context)
