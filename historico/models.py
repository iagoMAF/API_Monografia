from django.db import models
from datetime import datetime

class Historico(models.Model):
    data = models.DateTimeField(auto_now=True, verbose_name='Data')
    usuario = models.CharField(max_length=255, verbose_name='Nome do usuário')
    tipoAcao = models.CharField(max_length=1, verbose_name='Tipo Ação')
    descAcao = models.CharField(max_length=255, verbose_name='Descrição da ação')
    tabela = models.CharField(max_length=255, verbose_name='Tabela alterada')
    idElemento = models.IntegerField(verbose_name='Id do elemento alterado')

    def __str__(self):
        return f"{self.nome} ({self.nivel})"