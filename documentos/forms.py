from django import forms
from . models import Documentos, Areas
from equipe.models import Pesquisador

class DocumentosForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(DocumentosForm, self).__init__(*args, **kwargs)
    self.fields['areaConcentracao'].widget.choices = [(choice[0], choice[0]) for choice in Areas.choices]
    #self.fields['autor'].widget.choices = [(choice[0], choice[0]) for choice in Pesquisador.objects.all()]
    #if self.instance.pk:
    #      self.fields['autor'].initial = self.instance.autor.values_list('id', flat=True)
  
  class Meta:
    model = Documentos
    fields = ['titulo', 'autor', 'orientador', 'coorientador','resumo', 'dataEntrega', 'arquivo', 'notaFinal', 'areaConcentracao', 'palavrasChaves']
    widgets = {
      'titulo': forms.TextInput(attrs={'placeholder': 'Entre com o titulo da monografia'}),
      'dataEntrega': forms.DateInput(attrs={'id': 'dataAtualCampo'}),
      'arquivo': forms.FileInput(attrs={'id': 'arquivo'}),
      'notaFinal': forms.NumberInput(attrs={'placeholder': 'Entre com a nota final da monografia'}),
      'palavrasChaves': forms.Textarea(attrs={'placeholder': 'Entre com as palavras-chaves da monografia'})
    }
    
    

    