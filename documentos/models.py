from django.db import models
from django.core.exceptions import ValidationError
from equipe.models import Pesquisador

# Create your models here.
AREAS_CHOICES = [
    ("CSH","Ciências Sociais e Humanas"),
    ("CET","Ciências Exatas e Tecnológicas"),
    ("CSE","Ciências da Saúde"),
    ("CBA","Ciências Biológicas e Ambientais"),
    ("ACO","Artes e Comunicação"),
    ("EAO","Economia e Administração"),
    ("EDU","Educação"),
    ("DCJ","Direito e Ciências Jurídicas"),
    ("TIC","Tecnologia da Informação e Ciência da Computação"),
] 
class Areas(models.TextChoices):
    CSH = 'Ciências Sociais e Humanas'
    CET = 'Ciências Exatas e Tecnológicas'
    CSE = 'Ciências da Saúde'
    CBA = 'Ciências Biológicas e Ambientais'
    ACO = 'Artes e Comunicação'
    EAO = 'Economia e Administração'
    EDU = 'Educação'
    DCJ = 'Direito e Ciências Jurídicas'
    TIC = 'Tecnologia da Informação e Ciência da Computação'

class Documentos(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='Titulo da Monografia')
    autor = models.ManyToManyField(Pesquisador, related_name='autor_requests_created')
    orientador= models.ManyToManyField(Pesquisador, related_name='orientador_requests_created')
    coorientador = models.ManyToManyField(Pesquisador, related_name='coorientador_requests_created')
    resumo = models.TextField(verbose_name='Resumo')
    palavrasChaves = models.TextField(verbose_name='Palavras-chaves')
    dataEntrega = models.DateTimeField(verbose_name='Data de Entrega')
    arquivo = models.FileField(upload_to='documentos/pdfs/', blank=True, verbose_name='Documento em PDF')
    notaFinal = models.FloatField(null=True, blank=True, verbose_name='Nota final')
    areaConcentracao = models.CharField(max_length=50, null=True, blank=True, choices=Areas.choices, verbose_name='Área de Concentração')
    def areaConcentracaoNome(self):
        return dict(Areas.choices)[self.areaConcentracao]

    def __str__(self):
        autores = ', '.join([str(pesquisador) for pesquisador in self.autor.all()])
        # area_concentracao_display = dict(Areas.choices)[self.areaConcentracao]
        return f"{self.titulo} ({self.palavrasChaves}) - Autores: {autores}"
    