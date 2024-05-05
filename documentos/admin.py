from django.contrib import admin
from .models import Documentos

class DocumentosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'resumo', 'areaConcentracao', 'dataEntrega', 'notaFinal')
    list_filter = ('titulo', 'autor', 'orientador', 'palavrasChaves', 'dataEntrega', 'notaFinal')  # Filtro para o campo areaConcentracao
    list_per_page = 10
    ordering = ('titulo', )

admin.site.register(Documentos, DocumentosAdmin)
