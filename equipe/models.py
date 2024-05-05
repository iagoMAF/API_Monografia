from django.db import models
from datetime import datetime

# Create your models here.
class Titulacao(models.TextChoices):
    GRADUANDO = 'Graduando'
    GRADUACAO = 'Graduação' 
    MESTRADO = 'Mestrado'
    DOUTORADO = 'Doutorado'

class Pesquisador(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome do Pesquisador')
    nivel = models.CharField(max_length=10, choices=Titulacao.choices, verbose_name='Titulação')
    lattes = models.URLField(blank=True, null=True, verbose_name='Lattes')
    linkedin = models.URLField(blank=True, null=True, verbose_name='Linkedin')
    researchgate = models.URLField(blank=True, null=True, verbose_name='Research Gate')
    email = models.EmailField(verbose_name='E-mail')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação')
    ativo = models.BooleanField(default=False)

    CARGO = {
        'ALUNO': 'Aluno',
        'PROFESSOR': 'Professor',
        'TECNICO': 'Técnico',
    }

    cargo = models.CharField(max_length=10, choices=CARGO, verbose_name='Cargo')

    def __str__(self):
        return f"{self.nome} ({self.nivel})"