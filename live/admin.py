from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
    list_display = ('client', 'type', 'competition', 'evenement', 'titre', 'teams',  'date_creation', 'action', 'author')




admin.site.register(ClientLive)
admin.site.register(TypeLive)
admin.site.register(CompetitionLive)
admin.site.register(TeamsLive)
