from rest_framework import serializers
from .models import Documentos

class DocumentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentos
        fields = '__all__'
