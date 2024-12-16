from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UtilizadorForm, MinhaContaForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model, update_session_auth_hash

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UtilizadorForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('home')
    else:
        form = UtilizadorForm()
    return render(request, 'registar.html', {'form': form})

class LoginUtilizador(LoginView):
    template_name = "login.html"

# class LogoutUtilizador(LogoutView):

#     next_page = "home"

def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    """
    View para lidar com o login de utilizadores.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Obter o modelo de usuário ativo
        User = get_user_model()

        # Verificar se o utilizador existe
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Mensagem de erro se o utilizador não existir
            messages.error(request, 'O utilizador não existe.')
            return render(request, 'login.html')

        # Verificar a senha
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirecionar para a página inicial
        else:
            # Mensagem de erro se a senha estiver incorreta
            messages.error(request, 'Palavra-passe incorreta.')
            return render(request, 'login.html')

    return render(request, 'login.html')

@login_required
def minha_conta(request):
    return render(request, 'minha_conta.html', {'utilizador': request.user})

@login_required
def editar_conta(request):
    if request.method == 'POST':
        form = MinhaContaForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua conta foi atualizada com sucesso!')
            return redirect('minha_conta')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = MinhaContaForm(instance=request.user)
    return render(request, 'editar_conta.html', {'form': form})