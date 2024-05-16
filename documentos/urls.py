from django.urls import path
from . import views

urlpatterns = [
    path('documentos/pdfs/<str:filename>/', views.view_pdf, name='view_pdf'),
    path('documentos/', views.listar_documentos, name='listar_documentos'),
    path('documentos/adicionar/', views.adicionar_documento, name='adicionar_documento'),
    path('documentos/atualizar/<int:documento_id>/', views.atualizar_documento, name='atualizar_documento'),
    path('documentos/excluir/<int:documento_id>/', views.excluir_documento, name='excluir_documento'),
    
    # API
    path('api/documentos/', views.listar_documentosAPI, name='listar_documentosAPI'),
    path('api/documentos/cadastro/', views.cadastra_documento, name='cadastra_documento'),
    path('api/documentos/atualiza/<int:pk>/', views.atualiza_documento, name='atualiza_documento'),
    path('api/documentos/excluir/<int:pk>/', views.exclui_documento, name='exclui_documento'),
    path('api/documentos/<int:pk>/', views.detalhe_documento, name='detalhe_documento'),
] 