from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from live.models import *
from hight_live.models import *
from extra_live.models import *


# Chart js country
from .models import *
from .forms import *

from django.db.models.functions import ExtractMonth
from collections import Counter

from django.db.models import Count
import json
from django.db.models.functions import TruncMonth



def statistic_view(request):

    tahe_live = Tache.objects.all().count()
    tahe_hl = TacheHlive.objects.all().count()
    tahe_extra = TacheExtraLive.objects.all().count()

    # Nombre de tâches actives et bloquées
    bloque = Tache.objects.filter(action='a_creer').count()
    actifs = Tache.objects.filter(action='creer').count()

    bloque_hl = TacheHlive.objects.filter(action='a_creer').count()
    actifs_hl = TacheHlive.objects.filter(action='creer').count()

    bloque_extra = TacheExtraLive.objects.filter(action='a_creer').count()
    actifs_extra = TacheExtraLive.objects.filter(action='creer').count()




    ########################################################################LIVE
    # Récupérer les mois et compter le nombre de LIVE créées pour chaque mois
    taches_per_month = Tache.objects.annotate(month=TruncMonth('date_creation')).values('month').annotate(count=Count('id'))
    # Préparer les données pour le graphique
    months = [tache['month'].strftime('%B-%Y') for tache in taches_per_month]
   
    dates = Tache.objects.values_list('date_creation', flat=True)
    mois = [date.strftime('%B-%Y') for date in dates]
    # Compter le nombre de tâches par mois
    counts = Counter(mois)
    ########################################################################LIVE


    ########################################################################HL
    taches_per_month_hl = TacheHlive.objects.annotate(month=TruncMonth('date_creation')).values('month').annotate(count=Count('id'))
    # Préparer les données pour le graphique
    months_hl = [tache['month'].strftime('%Y-%m') for tache in taches_per_month_hl]

    dates = TacheHlive.objects.values_list('date_creation', flat=True)
    mois = [date.strftime('%B-%Y') for date in dates]
    # Compter le nombre de tâches par mois
    counts_hl = Counter(mois)
    ########################################################################HL


    ########################################################################EXTRA
    # Récupérer les mois et compter le nombre de EXTRA créées pour chaque mois
    taches_per_month_extra = TacheExtraLive.objects.annotate(month=TruncMonth('date_creation')).values('month').annotate(count=Count('id'))

    # Préparer les données pour le graphique
    months_extra = [tache['month'].strftime('%Y-%m') for tache in taches_per_month_extra]

    dates = TacheExtraLive.objects.values_list('date_creation', flat=True)
    mois = [date.strftime('%B-%Y') for date in dates]
    # Compter le nombre de tâches par mois
    counts_extra = Counter(mois)
    ########################################################################HL

  






    context = {
        'tahe_live': tahe_live,
        'tahe_hl': tahe_hl,
        'tahe_extra': tahe_extra,

        'actifs': actifs,
        'bloque': bloque,

        'actifs_hl': actifs_hl,
        'bloque_hl': bloque_hl,

        'actifs_extra': actifs_extra,
        'bloque_extra': bloque_extra,


        'months': json.dumps(months),
        'counts': json.dumps(counts),

        'months_hl': json.dumps(months_hl),
        'counts_hl': json.dumps(counts_hl),

        'months_extra': json.dumps(months_extra),
        'counts_extra': json.dumps(counts_extra),


    }


    return render(request, "statistic/statistic.html", context)



