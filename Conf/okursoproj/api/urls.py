from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('programacao/', programacao, name='list-courses-programmer'),
    path('design/', design, name='list-courses-design'),
    path('edicao/', edicao, name='list-courses-edicao'),
    path('devops/', devops, name='list-courses-devops'),
    path('ciencia-dados/', ciencia_dados, name='list-courses-ciencia-dados'),
    path('cadastroUsuario/', cadastroUsuario, name='insert-user'),
    path('efetuarCompra/', efetuarCompra, name='buy-Order'),
    path('meusCursos/', meusCursos, name ='my-cousers'),
    path('Modulos/', meusCursos, name ='my-modules'),
    path('Aulas/', minhasAulas, name ='my-modules')
]