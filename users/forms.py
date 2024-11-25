from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilizador

class UtilizadorForm(UserCreationForm):
    """
    Formulário para criar um novo utilizador.

    Campos:
        email (EmailField): O endereço de e-mail do utilizador, que é obrigatório.
    """
    email = forms.EmailField(required=True)
    
    class Meta:
        """
        Metadados para o formulário de utilizador.

        Atributos:
            model (Utilizador): O modelo associado a este formulário.
            fields (list): A lista de campos a serem exibidos no formulário.
        """
        model = Utilizador
        fields = ['username', 'email', 'password1', 'password2']
        
    def clean_email(self):
        """
        Valida o campo de e-mail.

        Verifica se o e-mail já está em uso e levanta uma ValidationError se estiver.

        Retorna:
            str: O e-mail validado.
        
        Lança o erro:
            forms.ValidationError: Se o e-mail já estiver em uso.
        """
        email = self.cleaned_data.get('email')
        if Utilizador.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email