from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_historico, name='listar_historico'),
    path('id=<int:elemento_id>&tipo=<str:elemento_tipo>/', views.historico_documento, name='historico_elemento'),
]
