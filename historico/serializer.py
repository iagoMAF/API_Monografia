from rest_framework import serializers
from .models import Historico

class PesquisadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = '__all__'
 