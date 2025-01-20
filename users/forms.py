from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilizador

class UtilizadorForm(UserCreationForm):
    """
    Formulário para criar um novo utilizador.

    Campos:
        first_name (CharField): O primeiro nome do utilizador, obrigatório.
        last_name (CharField): O sobrenome do utilizador, obrigatório.
        email (EmailField): O endereço de e-mail do utilizador, obrigatório.
    """
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=100, label="Nome")
    last_name = forms.CharField(required=True, max_length=100, label="Apelido")

    class Meta:
        """
        Metadados para o formulário de utilizador.

        Atributos:
            model (Utilizador): O modelo associado a este formulário.
            fields (list): A lista de campos a serem exibidos no formulário.
        """
        model = Utilizador
        fields = ['first_name', 'last_name', 'username', 'email', 'telefone', 'password1', 'password2']

    def clean_email(self):
        """
        Valida o campo de e-mail.

        Verifica se o e-mail já está em uso e levanta uma ValidationError se estiver.

        Retorna:
            str: O e-mail validado.
        
        Lança:
            forms.ValidationError: Se o e-mail já estiver em uso.
        """
        email = self.cleaned_data.get('email')
        if Utilizador.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email
    
    def clean_username(self):
        """
        Valida o campo de nome de utilizador.
        Levanta uma ValidationError se o nome de utilizador já estiver em uso.
        """
        username = self.cleaned_data.get('username')
        if Utilizador.objects.filter(username=username).exists():
            raise forms.ValidationError("Nome de utilizador já está em uso.")
        return username
    
    def clean_password2(self):
        """
        Valida se as palavras-passe são iguais.

        Lança um erro de validação se as palavras-passe não coincidirem.

        Retorna:
            Mensagem de erro: As palavras-passe não coincidem.
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            raise forms.ValidationError("As palavras-passe não coincidem.")
        
        return password2
    
class MinhaContaForm(forms.ModelForm):
    """
    Formulário para atualizar a conta do usuário.

    Metadados:
        model (Utilizador): O modelo associado a este formulário.
        fields (tuple): A lista de campos a serem exibidos no formulário.
    """
    class Meta:
        """
        Metadados para o formulário de conta do usuário.

        Atributos:
            model (Utilizador): O modelo associado a este formulário.
            fields (tuple): A lista de campos a serem exibidos no formulário.
        """
        model = Utilizador
        fields = ('first_name', 'last_name', 'username','email', 'telefone')