from django.urls import path
from .views import *


app_name = 'hight_live'
urlpatterns = [

    path('', TacheListView.as_view(), name='list_live'),
    path('hl_modify/<int:pk>', TacheModifyHlViews.as_view(), name='hl_modify'),
    path('hl_detail/<int:pk>', TacheDetailHlView.as_view(), name='hl_detail'),
    path('hl_delete/<int:pk>', TacheDeleteHlViews.as_view(), name='hl_delete'),
    path('create_campagnesHl/', create_campagnesHl_view, name='create_campagnesHl'),
    path('tache_hl/', tache_hl_view, name='tache_hl'),



]