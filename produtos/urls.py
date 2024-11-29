from pata_feliz import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('lista_produtos', views.lista_produtos, name='lista_produtos'),
    path('criar/', views.criar_produto, name='criar_produto'),
    path('ver/<str:produto_slug>/', views.ver_produto, name='ver_produto'),
    path('editar/<str:produto_slug>/', views.editar_produto, name='editar_produto'),
    path('apagar/<str:produto_slug>/', views.apagar_produto, name='apagar_produto'),

    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('criar_categoria/', views.criar_categoria, name='criar_categoria'),
    path('editar_categoria/<str:categoria_slug>/', views.editar_categoria, name='editar_categoria'),
    path('ver_categoria/<str:categoria_slug>/', views.ver_categoria, name='ver_categoria'),
    path('apagar_categoria/<str:categoria_slug>/', views.apagar_categoria, name='apagar_categoria'),
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
