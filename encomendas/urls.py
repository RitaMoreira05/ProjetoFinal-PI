from django.urls import path
from . import views

urlpatterns = [
    path('historico/', views.historico_encomendas, name='historico_encomendas'),
    path('detalhes/<int:encomenda_id>/', views.detalhes_encomendas, name='detalhes_encomendas'),
]