from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from documentos.models import Documentos
from documentos.forms import DocumentosForm
from equipe.models import Pesquisador
from django.db.models import Count
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Create your views here.
def show_dashboard(request):
    # Para o gráfico de barras
    areas = [choice[0] for choice in Documentos._meta.get_field('areaConcentracao').choices]
    documentos_por_area = [Documentos.objects.filter(areaConcentracao=area).count() for area in areas]

    # Para o gráfico de pizza
    titulacoes = [choice[0] for choice in Pesquisador._meta.get_field('nivel').choices]
    pesquisadores_por_titulacao = [Pesquisador.objects.filter(nivel=titulacao).count() for titulacao in titulacoes]

    #Para o grafico de docuemntos por nota
    documentos_por_nota = Documentos.objects.exclude(notaFinal__isnull=True).values('notaFinal').annotate(total=Count('id')).order_by('-notaFinal')
    notas = [item['notaFinal'] for item in documentos_por_nota]
    quantidade_documentos = [item['total'] for item in documentos_por_nota]

    #Quantidade de doumentos por autor
    autores = Pesquisador.objects.annotate(num_documentos=Count('autor_requests_created')).order_by('-num_documentos')
    nomes_autores = [autor.nome for autor in autores]
    documentos_por_autor = [autor.num_documentos for autor in autores]

    #nuvem de palavras 
    palavras_chaves = ' '.join([doc.palavrasChaves for doc in Documentos.objects.all()])
    if palavras_chaves: 
        print(palavras_chaves)
        wordcloud = WordCloud(background_color='white', width=800, height=400).generate(palavras_chaves)
        
        # Salve a imagem em um arquivo
        wordcloud.to_file('static/images/wordcloud.png')
    
        file_exists = True
    else: 
        file_exists = False

    context = {
        'areas': areas,
        'documentos_por_area': documentos_por_area,
        'titulacoes': titulacoes,
        'pesquisadores_por_titulacao': pesquisadores_por_titulacao,
        'notas': notas,
        'quantidade_documentos': quantidade_documentos,
        'nomes_autores': nomes_autores,
        'documentos_por_autor': documentos_por_autor,
        'arquivo_existe': file_exists,
    }
    


    return render(request, 'dashboard.html', context)