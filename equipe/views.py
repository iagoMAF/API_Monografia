from django.shortcuts import render
from .models import Pesquisador
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import PesquisadorSerializer

def listar_equipe(request):
    pesquisadores = Pesquisador.objects.all()
    return render(request, 'equipe.html', {'pesquisadores': pesquisadores}) 

@api_view(['GET'])
def listar_pesquisadoresJson(request):
    pesquisadores = Pesquisador.objects.all()
    serializer = PesquisadorSerializer(pesquisadores, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def cadastrar_pesquisadorJson(request):
    serializer = PesquisadorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detalhe_pesquisadorJson(request, pk):
    try:
        pesquisador = Pesquisador.objects.get(pk=pk)
    except Pesquisador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PesquisadorSerializer(pesquisador)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def atualizar_pesquisadorJson(request, pk):
    try:
        pesquisador = Pesquisador.objects.get(pk=pk)
    except Pesquisador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PesquisadorSerializer(pesquisador, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def excluir_pesquisadorJson(request, pk):
    try:
        pesquisador = Pesquisador.objects.get(pk=pk)
    except Pesquisador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    pesquisador.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)