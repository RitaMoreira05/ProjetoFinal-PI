from django.urls import path
from . import views

urlpatterns = [
    path('adicionar_carrinho/<slug:produto_slug>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('ver_carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('remover_carrinho/<slug:produto_slug>/', views.remover_do_carrinho, name='remover_carrinho'),
    path('atualizar_quantidade/<slug:produto_slug>/', views.atualizar_quantidade, name='atualizar_quantidade'),
]