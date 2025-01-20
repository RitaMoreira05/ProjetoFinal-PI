from django.urls import path
from . import views

urlpatterns = [
    path('agendar_consulta/', views.agendar_consulta, name='agendar_consulta'),
]
