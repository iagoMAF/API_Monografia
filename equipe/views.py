from django.shortcuts import render
from .models import Pesquisador
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import status
from .serializer import PesquisadorSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

def listar_equipe(request):
    pesquisadores = Pesquisador.objects.all()
    return render(request, 'equipe.html', {'pesquisadores': pesquisadores}) 

@swagger_auto_schema(methods=['GET'], operation_summary="Listar todos os pesquisadores", tags=['Equipe'])
@api_view(['GET'])
def listar_pesquisadoresJson(request):
    """
    Lista todos os pesquisadores.
    """
    pesquisadores = Pesquisador.objects.all()
    serializer = PesquisadorSerializer(pesquisadores, many=True)
    return Response(serializer.data)

@swagger_auto_schema(methods=['POST'], operation_summary="Cadastrar um novo pesquisador", request_body=PesquisadorSerializer, tags=['Equipe'])
@api_view(['POST'])
def cadastrar_pesquisadorJson(request):
    """
    Cadastra um novo pesquisador.
    """
    serializer = PesquisadorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods=['GET'], operation_summary="Detalhar um pesquisador", tags=['Equipe'])
@api_view(['GET'])
def detalhe_pesquisadorJson(request, pk):
    """
    Retorna os detalhes de um pesquisador específico.
    """
    try:
        pesquisador = Pesquisador.objects.get(pk=pk)
    except Pesquisador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PesquisadorSerializer(pesquisador)
    return Response(serializer.data)

@swagger_auto_schema(methods=['PUT', 'PATCH'], operation_summary="Atualizar um pesquisador existente", request_body=PesquisadorSerializer, tags=['Equipe'])
@api_view(['PUT', 'PATCH'])
def atualizar_pesquisadorJson(request, pk):
    """
    Atualiza os detalhes de um pesquisador existente.
    """
    try:
        pesquisador = Pesquisador.objects.get(pk=pk)
    except Pesquisador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PesquisadorSerializer(pesquisador, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods=['DELETE'], operation_summary="Excluir um pesquisador existente", tags=['Equipe'])
@api_view(['DELETE'])
def excluir_pesquisadorJson(request, pk):
    """
    Exclui um pesquisador existente.
    """
    try:
        pesquisador = Pesquisador.objects.get(pk=pk)
    except Pesquisador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    pesquisador.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
