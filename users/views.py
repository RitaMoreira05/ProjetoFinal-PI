from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UtilizadorForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UtilizadorForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('base')
    else:
        form = UtilizadorForm()
    return render(request, 'registar.html', {'form': form})

class LoginUtilizador(LoginView):
    template_name = "login.html"

class LogoutUtilizador(LogoutView):
    next_page = "base"

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    """
    View para lidar com o login de utilizadores.

    Args:
        request (HttpRequest): O objeto de solicitação HTTP.

    Returns:
        HttpResponse: A resposta HTTP com o formulário de login ou redirecionamento após o login bem-sucedido.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirecionar para a página inicial ou outra página após o login
        else:
            error_message = 'Nome de utilizador ou senha incorretos.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')