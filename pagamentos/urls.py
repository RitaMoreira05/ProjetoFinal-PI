from django.urls import path
from . import views

urlpatterns = [
    path('nova/', views.nova_compra, name='nova_compra'),
    path('finalizar/', views.finalizar_compra, name='finalizar_compra'),
    path('sucesso/', views.finalizar_compra, name='compra_sucesso'),
    path('falhada/', views.finalizar_compra, name='compra_falhada'),
]
