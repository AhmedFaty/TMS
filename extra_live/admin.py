from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(TacheExtraLive)
class TacheAdmin(admin.ModelAdmin):
    list_display = ('client', 'type', 'competition', 'evenement', 'titre', 'teams',  'date_creation', 'action', 'author')




admin.site.register(ClientExtra)
admin.site.register(TypeExtra)
admin.site.register(CompetitionExtra)
admin.site.register(TeamsExtra)
