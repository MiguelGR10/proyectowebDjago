from django.contrib import admin
from servicios.models import servicios

class serad(admin.ModelAdmin):
    readonly_fields=('created', 'update')
    list_display=("titulo", "contenido", "update")
    search_fields=("titulo",)
    list_filter=("update",)

admin.site.register(servicios, serad)
