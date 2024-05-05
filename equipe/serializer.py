from rest_framework import serializers
from .models import Pesquisador

class PesquisadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesquisador
        fields = ['id', 'nome', 'nivel', 'lattes', 'linkedin', 'researchgate', 'email', 'data_criacao', 'ativo', 'cargo']
 