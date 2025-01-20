from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Encomenda, ItemEncomenda
from django.contrib import messages

@login_required
def historico_encomendas(request):
    encomendas = Encomenda.objects.filter(user=request.user).order_by('-data')
    return render(request, 'historico_encomendas.html', {'encomendas': encomendas})


@login_required
def detalhes_encomendas(request, encomenda_id):
    encomenda = get_object_or_404(Encomenda, id=encomenda_id, user=request.user)
    itens = ItemEncomenda.objects.filter(encomenda=encomenda)
    return render(request, 'detalhes_encomendas.html', {
        'encomenda': encomenda,
        'itens': itens
    })

def listar_encomendas(request):
    if request.user.is_staff:  # Verifica se o usuário é administrador
        encomendas = Encomenda.objects.all()
    else:
        encomendas = Encomenda.objects.filter(user=request.user)
    
    return render(request, 'listar_encomendas.html', {
        'encomendas': encomendas,
    })

@login_required
def alterar_estado(request, encomenda_id):
    if request.user.is_staff:
        encomenda = get_object_or_404(Encomenda, id=encomenda_id)
        
        if request.method == 'POST':
            novo_estado = request.POST.get('estado')
            if novo_estado:
                encomenda.estado = novo_estado
                encomenda.save()
                messages.success(request, 'Estado da encomenda alterado com sucesso.')
                return redirect('listar_encomendas')
        
        return render(request, 'alterar_estado.html', {
            'encomenda': encomenda,
        })
    else:
        messages.error(request, "Acesso restrito.")
        return redirect('home')