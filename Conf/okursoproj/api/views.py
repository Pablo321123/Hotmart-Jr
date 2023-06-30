import json
from django.shortcuts import render
from django.http import HttpResponse

# Django Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Campos serializados
from .serializers import *

#Metodos GET
@api_view(['GET'])
def programacao(request):

    serialized_programacao = ProgramacaoSerializer.serializerCourses(
        'programacao')
    return Response(serialized_programacao, status=status.HTTP_200_OK)
    # return HttpResponse('OK')

@api_view(['GET'])
def design(request):

    serialized_programacao = ProgramacaoSerializer.serializerCourses('design')
    return Response(serialized_programacao, status=status.HTTP_200_OK)
    # return HttpResponse('OK')

@api_view(['GET'])
def edicao(request):

    serialized_programacao = ProgramacaoSerializer.serializerCourses('edicao')
    return Response(serialized_programacao, status=status.HTTP_200_OK)

@api_view(['GET'])
def devops(request):

    serialized_programacao = ProgramacaoSerializer.serializerCourses('devops')
    return Response(serialized_programacao, status=status.HTTP_200_OK)

@api_view(['GET'])
def ciencia_dados(request):
    # cdc = ciencia de dados -> Categoria no banco Mysql
    serialized_programacao = ProgramacaoSerializer.serializerCourses('cd')
    return Response(serialized_programacao, status=status.HTTP_200_OK)


#Métodos POST
@api_view(['POST'])
def cadastroUsuario(request):
    # cdc = ciencia de dados -> Categoria no banco Mysql
    if request.data:
        # print(f"{request.data['nome']}, {request.data['email']}, {request.data['cpf']}, {request.data['senha']}")
        serialized_insert = ProgramacaoSerializer.inserirUsuario(
            request.data["nome"], request.data["email"], request.data["cpf"], request.data["senha"])
        if serialized_insert:
            return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def efetuarCompra(request):
    try:
        if request.data:
            idCompra = ProgramacaoSerializer.getNextIDCompra()
            for r in request.data:
                serialized_insert = ProgramacaoSerializer.efetuarCompra(
                    idCompra, r['formaDePagamento'], r['precoVenda'], r['codCupom'], r['codCurso'], r['comprador'])
            return Response(status=status.HTTP_200_OK)
        
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    # serialized_make = ProgramacaoSerializer.efetuarCompra()

@api_view(['POST'])
def meusCursos(request):
    # cdc = ciencia de dados -> Categoria no banco Mysql
    if request.data:
        serialized_cousers = ProgramacaoSerializer.getMyCourses(request.data['cpf'])
    return Response(serialized_cousers, status=status.HTTP_200_OK)

@api_view(['POST'])
def meusCursos(request):
    # cdc = ciencia de dados -> Categoria no banco Mysql
    if request.data:
        serialized_cousers = ProgramacaoSerializer.getModules(request.data['idCurso'])
    return Response(serialized_cousers, status=status.HTTP_200_OK)

@api_view(['POST'])
def minhasAulas(request):
    # cdc = ciencia de dados -> Categoria no banco Mysql
    if request.data:
        serialized_cousers = ProgramacaoSerializer.getClass(request.data['idCurso'], request.data['idModulo'])
    return Response(serialized_cousers, status=status.HTTP_200_OK)


