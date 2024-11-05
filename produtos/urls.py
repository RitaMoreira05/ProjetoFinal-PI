from pata_feliz import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('criar/', views.criar_produto, name='criar_produto'),
    path('ver/<int:produto_id>/', views.ver_produto, name='ver_produto'),
    path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('apagar/<int:produto_id>/', views.apagar_produto, name='apagar_produto'),

    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/<int:categoria_id>/', views.ver_categoria, name='ver_categoria'),
    path('editar_categorias/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('criar_categoria/', views.criar_categoria, name='criar_categoria'),
    path('apagar_categoria/<int:categoria_id>/', views.apagar_categoria, name='apagar_categoria'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
