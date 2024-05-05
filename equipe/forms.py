from django import forms
from equipe.models import Pesquisador

class PesquisadorForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(PesquisadorForm, self).__init__(*args, **kwargs)
    #self.fields['areaConcentracao'].widget.choices = [(choice[0], choice[0]) for choice in Areas.choices]
    #self.fields['autor'].widget.choices = [(choice[0], choice[0]) for choice in Pesquisador.objects.all()]
    #if self.instance.pk:
    #      self.fields['autor'].initial = self.instance.autor.values_list('id', flat=True)
  
  class Meta:
    model = Pesquisador
    fields = ['nome', 'nivel', 'lattes', 'linkedin','researchgate', 'email', 'ativo']
    widgets = {
      'nome': forms.TextInput(attrs={'placeholder': 'Entre com o nome'}),
      'email': forms.EmailInput(attrs={'placeholder': 'Entre com e-mail'}),
      'data_criacao': forms.DateField(disabled=True),
      'ativo': forms.CheckboxInput(attrs={'placeholder': 'Usuário Ativo?'}),
      'lattes': forms.TextInput(attrs={'placeholder': 'Entre com lattes'}),
      'linkedin': forms.TextInput(attrs={'placeholder': 'Entre com o linkd do Linkedin'}),
      'researchgate': forms.TextInput(attrs={'placeholder': 'Entre com o Search Gateway'}),
    }
    
    

    