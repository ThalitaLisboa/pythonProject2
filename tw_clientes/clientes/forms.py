from django import forms
from .models import Cliente, Endereco

# formulario para validar antes de ir para o banco de dados. essa é a validação do backend
class ClienteForm(forms.ModelForm):
    #nome = forms.CharField(widget=forms.Textarea()) para deixar com um campo maior.
    class Meta:
        model = Cliente
        fields = ['nome', 'sexo', 'data_nascimento', 'email', 'profissao']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'pais']
