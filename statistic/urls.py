from django.urls import path
from .views import *




app_name = 'statistic'
urlpatterns = [

    path('', statistic_view, name='statistic'),
    # path('chart', line_chart, name='line_chart'),
    # path('chartJSON', line_chart_json, name='line_chart_json'),

]

