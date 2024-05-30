from django.urls import path
from .views import *


app_name = 'live'
urlpatterns = [

    path('', TacheListLiveView.as_view(), name='tache_list'),
    path('create_campagnes/', create_campagnes_view, name='create_campagnes'),
    path('detail/<int:pk>', TacheDetailView.as_view(), name='tache_detail'),
    path('modify/<int:pk>', TacheModifyViews.as_view(), name='tache_modify'),
    path('delete/<int:pk>', TacheDeleteViews.as_view(), name='tache_delete'),
    path('tache_live/', tache_live_view, name='tache_live'),




]