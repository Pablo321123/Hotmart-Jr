import json
from rest_framework import serializers
from .MySqlProxy import *


class ProgramacaoSerializer(serializers.Serializer):
    
    @staticmethod
    # converter os dados do curso de programacao para JSON
    def serializerCourses(categoria):

        okursoProxy = OKursoProxy('Pablo', '1234')
        responseProxy = okursoProxy.buscarCursos(categoria)

        print(categoria)

        if type(responseProxy) == str:
            return responseProxy
        else:
            rows = responseProxy
            result = []
            keys = ['nomeCurso', 'idCurso', 'autor',
                'descricao', 'valor', 'categoria', 'duracao']

            for row in rows:
                result.append(dict(zip(keys, row)))

            return result  # json.dumps(result)

    @staticmethod
    def inserirUsuario(nome, email, cpf, senha):
        okursoProxy = OKursoProxy('Pablo', '1234')
        reponseProxy = okursoProxy.insertUsuario(nome, email, cpf, senha)
            
        return reponseProxy

    @staticmethod
    def efetuarCompra():
        pass
       
    