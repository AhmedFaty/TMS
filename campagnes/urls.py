from django.urls import path
from .views import *


app_name = 'tache'
urlpatterns = [

    path('', TacheListView.as_view(), name='tache_list'),
    path('create_campagnes/', create_campagnes_view, name='create_campagnes'),
    path('detail/<int:pk>', TacheDetailView.as_view(), name='tache_detail'),
    path('modify/<int:pk>', TacheModifyViews.as_view(), name='tache_modify'),
    path('delete/<int:pk>', TacheDeleteViews.as_view(), name='tache_delete'),


]