from django.shortcuts import render, redirect
from .models import Historico
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import status
from .serializer import PesquisadorSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .forms import HistoricoForm

USUARIO = 'admin'

def historico_documento(request, elemento_id=None, elemento_tipo=None):
    historico = Historico.objects.filter(idElemento=elemento_id, tabela=elemento_tipo)
    return render(request, 'historico.html', {'Historicos': historico, 'historico_unico': True})   

def listar_historico(request):
    historico = Historico.objects.all()
    return render(request, 'historico.html', {'Historicos': historico, 'historico_unico': False}) 

def adicionar_historico(usuario, tabela, id):
    Historico.objects.create(
        usuario=usuario,
        tabela=tabela,
        idElemento=id,
        tipoAcao='C',
        descAcao='Criação'
    )
    
def remover_historico(usuario, tabela, id_elemento):
    Historico.objects.create(
        usuario=usuario,    
        tabela=tabela,
        idElemento=id_elemento,
        tipoAcao='D',
        descAcao='Exclusão'
    )
    
def atualiza_historico(usuario, tabela, itemAtualizado, itemAntigo):
    atualizacao = "Atualização: " 
    
    if tabela == 'Usuário':
        
        if itemAntigo.username != itemAtualizado.username:
            atualizacao = atualizacao + 'username, '
        if itemAntigo.first_name != itemAtualizado.first_name:
            atualizacao = atualizacao + 'nome, '
        if itemAntigo.last_name != itemAtualizado.last_name:
            atualizacao = atualizacao +'sobrenome, '
        if itemAntigo.email != itemAtualizado.email:
            atualizacao = atualizacao + 'e-mail, '
        if itemAntigo.is_staff != itemAtualizado.is_staff:
            atualizacao = atualizacao + 'nível de usuário, '
        if itemAntigo.password != itemAtualizado.password:
            atualizacao = atualizacao +'senha, '
            
        if atualizacao.endswith(", "):
            atualizacao = atualizacao[:-2]

        Historico.objects.create(
            usuario=usuario,
            tabela=tabela,
            idElemento=itemAtualizado.id,
            tipoAcao='U',
            descAcao=atualizacao
        )
    else:
        if tabela == 'Equipe':
            campos = [
                {'campo': 'nome', 'nome_exibicao': 'nome'},
                {'campo': 'nivel', 'nome_exibicao': 'nível'},
                {'campo': 'lattes', 'nome_exibicao': 'lattes'},
                {'campo': 'linkedin', 'nome_exibicao': 'linkedin'},
                {'campo': 'researchgate', 'nome_exibicao': 'research gate'},
                {'campo': 'email', 'nome_exibicao': 'e-mail'},
                {'campo': 'ativo', 'nome_exibicao': 'status de ativo'},
            ]
        elif tabela == 'Documento':
            campos = [           
                {'campo': 'titulo', 'nome_exibicao': 'título'},
                {'campo': 'autor', 'nome_exibicao': 'autor'},
                {'campo': 'orientador', 'nome_exibicao': 'orientador'},
                {'campo': 'coorientador', 'nome_exibicao': 'coorientador'},
                {'campo': 'resumo', 'nome_exibicao': 'resumo'},
                {'campo': 'dataEntrega', 'nome_exibicao': 'data de entrega'},
                {'campo': 'arquivo', 'nome_exibicao': 'arquivo'},
                {'campo': 'notaFinal', 'nome_exibicao': 'nota final'},
                {'campo': 'areaConcentracao', 'nome_exibicao': 'área de concentração'},
                {'campo': 'palavrasChaves', 'nome_exibicao': 'palavras-chave'}
            ]  
        
        for campo_info in campos:
            campo = campo_info['campo']
            nome_exibicao = campo_info['nome_exibicao']
            
            valor_atualizado = getattr(itemAtualizado.instance, campo)
            valor_antigo = getattr(itemAntigo, campo)

            # Compara os valores dos campos atualizado e antigo
            
            print('Novo: ' + str(valor_atualizado))
            print('Antigo: ' + str(valor_antigo))
            
            if valor_atualizado != valor_antigo:
                atualizacao += f"{nome_exibicao}, "

        if atualizacao.endswith(", "):
            atualizacao = atualizacao[:-2]

        Historico.objects.create(
            usuario=usuario,
            tabela=tabela,
            idElemento=itemAtualizado.instance.id,
            tipoAcao='U',
            descAcao=atualizacao
        )