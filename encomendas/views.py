from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Encomenda, ItemEncomenda

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