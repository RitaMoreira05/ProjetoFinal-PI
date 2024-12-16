from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import register, login_view, logout_view, minha_conta, editar_conta

urlpatterns = [
    path('registar/', register, name='registar'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('minha_conta/', minha_conta, name='minha_conta'),
    path('editar_conta/', editar_conta, name='editar_conta'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)