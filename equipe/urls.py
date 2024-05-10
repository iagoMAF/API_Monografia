from django.urls import path
from . import views

urlpatterns = [
    path('pesquisadores/', views.listar_equipe, name='listar_equipe'),
    path('pesquisadores/adicionar/', views.adicionar_equipe, name='adicionar_equipe'),
    path('pesquisadores/atualizar/<int:pesquisador_id>/', views.atualizar_equipe, name='atualizar_equipe'),
    path('pesquisadores/excluir/<int:pesquisador_id>/', views.excluir_equipe, name='excluir_equipe'),
    
    # API
    path('api/pesquisadores/', views.listar_pesquisadoresJson, name='listar_pesquisadoresJson'),
    path('api/pesquisadores/<int:pk>/', views.detalhe_pesquisadorJson, name='detalhe_pesquisadorJson'),
    path('api/pesquisadores/cadastrar/', views.cadastrar_pesquisadorJson, name='cadastrar_pesquisadorJson'),
    path('api/pesquisadores/atualizar/<int:pk>/', views.atualizar_pesquisadorJson, name='atualizar_pesquisadorJson'),
    path('api/pesquisadores/excluir/<int:pk>/', views.excluir_pesquisadorJson, name='excluir_pesquisadorJson'),
]
