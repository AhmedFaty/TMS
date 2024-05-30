from collections import Counter
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render,  get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import TacheForm
from .models import TacheHlive
from django.http import HttpResponseRedirect
from django.urls import reverse
import json


from django.db.models import Count
from django.db.models.functions import TruncMonth

from django.db.models.functions import ExtractMonth

from django.contrib.auth.decorators import login_required






# Create your views here.
class TacheListView(ListView):
    model = TacheHlive
    template_name = 'hight_live/tache_list_hl.html'
    context_object_name = 'taches'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Compter le nombre de tâches actives
        context['bloque'] = TacheHlive.objects.filter(action='a_creer').count()
        # Compter le nombre de tâches bloquées
        context['actifs'] = TacheHlive.objects.filter(action='creer').count()

        return context



    def get_queryset(self) -> QuerySet[Any]:
        return TacheHlive.objects.all().order_by('date_creation')
    

class TacheModifyHlViews(UpdateView):
    # form_class = TacheForm
    model = TacheHlive
    template_name = 'hight_live/tache_modifyhl.html'
    fields = ('client', 'type', 'competition', 'evenement', 'titre', 'teams', 'date_creation', 'action')
    
    def get_success_url(self) -> str:
        return reverse('hight_live:hl_detail', kwargs={'pk': self.object.pk})
    

class TacheDetailHlView(DetailView):
    model = TacheHlive
    # loolup_field = 'id'
    template_name = 'hight_live/tache_detailHl.html'
    context_object_name = 'taches'


class TacheDeleteHlViews(DeleteView):
    model = TacheHlive
    success_url = "/h_live/"
    template_name = 'hight_live/tache_deleteHl.html'


@login_required
def create_campagnesHl_view(request):

    user_connecte = request.user

    user_connecte = request.user
    form = TacheForm(request.POST or None, user=user_connecte)
    
    message = ''
    if form.is_valid():
        form.save()
        message = 'Campagne HL enregistrer avec success'
        form = TacheForm()
    context = {
        'form': form,
        'message': message
        }

    return render(request, "hight_live/campagneHl.html", context)
    


def tache_hl_view(request):

    ########################################################################TESTING
    # Récupérer les mois et compter le nombre de tâches créées pour chaque mois
    taches_per_month = TacheHlive.objects.annotate(month=TruncMonth('date_creation')).values('month').annotate(count=Count('id'))

    # Nombre de tache actif et creer
    bloque_hl = TacheHlive.objects.filter(action='a_creer').count()
    actifs_hl = TacheHlive.objects.filter(action='creer').count()
    tahe_hl = TacheHlive.objects.all().count()


    # Préparer les données pour le graphique
    months = [tache['month'].strftime('%Y-%m') for tache in taches_per_month]

    dates = TacheHlive.objects.values_list('date_creation', flat=True)
    mois = [date.strftime('%B-%Y') for date in dates]
    # Compter le nombre de tâches par mois
    counts = Counter(mois)




    context = {
        'months': json.dumps(months),
        'counts': json.dumps(counts),

        'actifs_hl': actifs_hl,
        'bloque_hl': bloque_hl,
        'tahe_hl': tahe_hl,

        
        
        }



    return render(request, 'hight_live/stat.html', context)