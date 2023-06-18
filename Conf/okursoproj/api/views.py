from django.shortcuts import render
from django.http import HttpResponse

#Django Rest Framework
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

#Campos serializados
from .serializers import *

# Create your views here.
@api_view(['GET'])
def programacao(request):    
    
    
    serialized_programacao = ProgramacaoSerializer.serializerCourses('programacao')
    return Response(serialized_programacao, status= status.HTTP_200_OK)
    #return HttpResponse('OK')    

# Create your views here.
@api_view(['GET'])
def design(request):    
        
    serialized_programacao = ProgramacaoSerializer.serializerCourses('design')
    return Response(serialized_programacao, status= status.HTTP_200_OK)
    #return HttpResponse('OK')   