
from django import forms
from historico.models import Historico


class HistoricoForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(HistoricoForm, self).__init__(*args, **kwargs)
  
  class Meta:
    model = Historico
    fields = ['usuario', 'tipoAcao', 'descAcao','tabela', 'idElemento']
    widgets = {
      'data': forms.DateField(disabled=True),
      'usuario': forms.TextInput(attrs={'placeholder': 'Entre com o nome do usuário'}),
      'tipoAcao': forms.TextInput(attrs={'placeholder': 'Entre com a sigla da ação'}),
      'descAcao': forms.TextInput(attrs={'placeholder': 'Descrição da ação'}),
      'tabela': forms.TextInput(attrs={'placeholder': 'Tabela modificada'}),
      'idElemento': forms.TextInput(attrs={'placeholder': 'Id do elemento modificado'}),
    }
###

    