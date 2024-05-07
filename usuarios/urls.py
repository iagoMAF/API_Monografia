from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path("atualizar/<int:usuario_id>/", views.atualizar_usuario, name="atualizar_usuario"),
    path("excluir/<int:usuario_id>/", views.excluir_usuario, name="excluir_usuario"),
    
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
