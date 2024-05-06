from django.urls import path
from . import views

urlpatterns = [
    path('pdfs/<str:filename>/', views.view_pdf, name='view_pdf'),
    path('', views.listar_documentos, name='listar_documentos'),
    path('adicionar/', views.adicionar_documento, name='adicionar_documento'),
    path('atualizar/<int:documento_id>/', views.atualizar_documento, name='atualizar_documento'),
    path('deletar/<int:documento_id>/', views.deletar_documento, name='deletar_documento'),
    
    # API
    path('api/documentos/', views.listar_documentosAPI, name='listar_documentosAPI'),
    path('api/<int:pk>/', views.detalhe_documento, name='detalhe_documento'),
] 