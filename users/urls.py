from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import register, LoginUtilizador, LogoutUtilizador 

urlpatterns = [
    path('registar/', register, name='registar'),
    path('login/', LoginUtilizador.as_view(), name='login'),
    path('logout/', LogoutUtilizador.as_view(), name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)