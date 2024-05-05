from django.urls import path
from . import views

urlpatterns = [
    path('pdfs/<str:filename>/', views.view_pdf, name='view_pdf'),
    path('', views.listar_documentos, name='listar_documentos'),
    path('api/documentos/', views.listar_documentosAPI, name='listar_documentosAPI'),
    path('api/<int:pk>/', views.detalhe_documento, name='detalhe_documento'),
] 