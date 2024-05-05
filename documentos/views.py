from django.shortcuts import render, redirect, get_object_or_404
from .models import Documentos
from django.http import FileResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from documentos.functions import handle_uploaded_file
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import DocumentosSerializer
from django.shortcuts import render
from .models import Documentos
import os
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

def view_pdf(request, filename):
    pdf_path = os.path.join('documentos/pdfs', filename)
    if os.path.exists(pdf_path):
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    else:
        return HttpResponseNotFound('PDF not found')
    
def listar_documentos(request):
    documentos = Documentos.objects.all()
    return render(request, 'documentosDataTable.html', {'documentos': documentos})

@swagger_auto_schema(method='get', responses={200: openapi.Response("List of Documentos", DocumentosSerializer(many=True))}, tags=['documentos'])
@api_view(['GET'])
def listar_documentosAPI(request):
    """
    Listar todos os documentos.
    """
    if request.method == 'GET':
        documentos = Documentos.objects.all()
        serializer = DocumentosSerializer(documentos, many=True)
        return Response(serializer.data)


@api_view(['DELETE', 'PUT', 'PATCH'])
def detalhe_documento(request, pk):
    try:
        documento = Documentos.objects.get(pk=pk)
    except Documentos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        documento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method in ['PUT', 'PATCH']:
        serializer = DocumentosSerializer(documento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


