from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path("atualizar/<int:usuario_id>/", views.atualizar_usuario, name="atualizar_usuario"),
    path("excluir/<int:usuario_id>/", views.excluir_usuario, name="excluir_usuario"),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('api/usuarios/', views.listar_usuariosJson, name='listar_usuariosJson'),
    path('api/usuarios/<int:usuario_id>', views.detalhe_usuarioJson, name='detalhe_usuarioJson'),
    path('api/usuarios/atualizar/<int:usuario_id>/', views.atualizar_usuarioJson, name='atualizar_usuarioJson'),
    path('api/usuarios/excluir/<int:usuario_id>/',views.excluir_usuarioJson, name='excluir_usuarioJson'),
    path('api/usuarios/cadastro/', views.cadastroJson, name='cadastroJson'),
    #path('api/usuarios/login/', views.loginJson, name='loginJson'),
    #path('api/usuarios/logout', views.logoutJson, name='logoutJson')
]
