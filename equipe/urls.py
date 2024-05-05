from django.urls import path
from . import views
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Sua API",
        default_version='v1',
        description="Descrição da sua API",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('', views.listar_equipe, name='listar_equipe'),
    path('api/pesquisadores/', views.listar_pesquisadoresJson, name='listar_pesquisadoresJson'),
    path('api/pesquisadores/<int:pk>/', views.detalhe_pesquisadorJson, name='detalhe_pesquisadorJson'),
    path('api/pesquisadores/cadastrar/', views.cadastrar_pesquisadorJson, name='cadastrar_pesquisadorJson'),
    path('api/pesquisadores/atualizar/<int:pk>/', views.atualizar_pesquisadorJson, name='atualizar_pesquisadorJson'),
    path('api/pesquisadores/excluir/<int:pk>/', views.excluir_pesquisadorJson, name='excluir_pesquisadorJson'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
