from django import forms
from .models import Compra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['valor', 'numero_cartao', 'nome_titular', 'validade', 'cvv']
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_numero_cartao(self):
        numero_cartao = self.cleaned_data.get('numero_cartao')
        if not numero_cartao.isdigit():
            raise forms.ValidationError("O número do cartão deve conter apenas dígitos.")
        return numero_cartao