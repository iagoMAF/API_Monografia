from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_equipe, name='listar_equipe'),
    path('api/pesquisadores/', views.listar_pesquisadoresJson, name='listar_pesquisadoresJson'),
    path('api/pesquisadores/<int:pk>/', views.detalhe_pesquisadorJson, name='detalhe_pesquisadorJson'),
    path('api/pesquisadores/cadastrar/', views.cadastrar_pesquisadorJson, name='cadastrar_pesquisadorJson'),
    path('api/pesquisadores/atualizar/<int:pk>/', views.atualizar_pesquisadorJson, name='atualizar_pesquisadorJson'),
    path('api/pesquisadores/excluir/<int:pk>/', views.excluir_pesquisadorJson, name='excluir_pesquisadorJson'),
]
