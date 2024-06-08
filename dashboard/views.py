from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from documentos.models import Documentos
from documentos.forms import DocumentosForm
from equipe.models import Pesquisador





# Create your views here.
def show_dashboard(request):
    # Para o gráfico de barras
    areas = [choice[0] for choice in Documentos._meta.get_field('areaConcentracao').choices]
    documentos_por_area = [Documentos.objects.filter(areaConcentracao=area).count() for area in areas]

    # Para o gráfico de pizza
    titulacoes = [choice[0] for choice in Pesquisador._meta.get_field('nivel').choices]
    pesquisadores_por_titulacao = [Pesquisador.objects.filter(nivel=titulacao).count() for titulacao in titulacoes]

    context = {
        'areas': areas,
        'documentos_por_area': documentos_por_area,
        'titulacoes': titulacoes,
        'pesquisadores_por_titulacao': pesquisadores_por_titulacao,
    }

    return render(request, 'dashboard.html', context)