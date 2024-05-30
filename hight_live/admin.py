from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(TacheHlive)
class TacheAdmin(admin.ModelAdmin):
    list_display = ('client', 'type', 'competition', 'evenement', 'titre', 'teams',  'date_creation', 'action', 'author')




admin.site.register(ClientHl)
admin.site.register(TypeHl)
admin.site.register(CompetitionHl)
admin.site.register(TeamsHl)
