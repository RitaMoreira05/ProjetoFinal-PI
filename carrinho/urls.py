from django.urls import path
from . import views

urlpatterns = [
    path('adicionar_carrinho/<slug:produto_slug>/', views.adicionar_ao_carrinho, name='adicionar_carrinho'),
    path('ver_carrinho/', views.ver_carrinho, name='ver_carrinho'),
]