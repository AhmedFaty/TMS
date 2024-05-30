from django.urls import path
from .views import *
from . import views



app_name = 'extra_live'
urlpatterns = [

    path('', TacheListView.as_view(), name='list_extra'),
    path('extra_detail/<int:pk>', TacheDetailExtraView.as_view(), name='extra_detail'),
    path('extra_modify/<int:pk>', TacheModifyExtraViews.as_view(), name='extra_modify'),
    path('extra_delete/<int:pk>', TacheDeleteExtraViews.as_view(), name='extra_delete'),
    path('create_campagnes_extra/', create_campagnes_extra_view, name='create_campagnes_extra'),
    path('tache_extra/', tache_extra_view, name='tache_extra'),




]