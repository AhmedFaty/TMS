from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render,  get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import TacheForm
from .models import Tache
from django.http import HttpResponseRedirect
from django.urls import reverse





def create_campagnes_view(request):
    form = TacheForm(request.POST or None)
    message = ''
    if form.is_valid():
        form.save()
        message = 'Campagne enregistrer avec success'
        form = TacheForm()
    context = {
        'form': form,
        'message': message
        }

    return render(request, "campagnes/campagne.html", context)


# Create your views here.
class TacheListView(ListView):
    model = Tache
    template_name = 'campagnes/tache_list.html'
    context_object_name = 'taches'
    # paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        return Tache.objects.all().order_by('date_creation')
    

class TacheDetailView(DetailView):
    model = Tache
    # loolup_field = 'id'
    template_name = 'campagnes/tache_detail.html'
    context_object_name = 'taches'


class TacheModifyViews(UpdateView):
    # form_class = TacheForm
    model = Tache
    template_name = 'campagnes/tache_modify.html'
    fields = ('client', 'type', 'competition', 'evenement', 'titre', 'date_creation', 'action')
    
    def get_success_url(self) -> str:
        return reverse('tache:tache_detail', kwargs={'pk': self.object.pk})
    

class TacheDeleteViews(DeleteView):
    model = Tache
    success_url = "/"
    template_name = 'campagnes/tache_delete.html'
    

    

