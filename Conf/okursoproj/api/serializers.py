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
    def getMyCourses(cpf):
        okursoProxy = OKursoProxy('Pablo', '1234')
        responseProxy = okursoProxy.getCourses(cpf)

        if type(responseProxy) == str:
            return responseProxy
        else:
            rows = responseProxy
            result = []
            keys = ['comprador', 'idCurso', 'nomeCurso',
                    'duracao', 'categoria', 'descricao', 'autor']

            for row in rows:
                result.append(dict(zip(keys, row)))

            return result  # json.dumps(result)

    @staticmethod
    def getModules(idCurso):
        okursoProxy = OKursoProxy('Pablo', '1234')
        responseProxy = okursoProxy.getModules(idCurso)

        if type(responseProxy) == str:
            return responseProxy
        else:
            rows = responseProxy
            result = []
            keys = ['idModulo', 'nome', 'descricao', 'codCurso']
            print(responseProxy)
            for row in rows:
                result.append(dict(zip(keys, row)))

            return result  # json.dumps(result)

    @staticmethod
    def getClass(idCurso, idModulo):
        okursoProxy = OKursoProxy('Pablo', '1234')
        responseProxy = okursoProxy.getClass(idCurso, idModulo)

        if type(responseProxy) == str:
            return responseProxy
        else:
            rows = responseProxy
            result = []
            keys = ['idAula', 'duracaoMinutos',
                    'numero', 'codModulo', 'nomeAula']
            print(responseProxy)
            for row in rows:
                result.append(dict(zip(keys, row)))

            return result  # json.dumps(result)

    @staticmethod
    def inserirUsuario(nome, email, cpf, senha):
        okursoProxy = OKursoProxy('Pablo', '1234')
        responseProxy = okursoProxy.insertUsuario(nome, email, cpf, senha)

        return responseProxy

    @staticmethod
    def efetuarCompra(idCompra, formaDePagamento, precoVenda, codCupom, codCurso, comprador):
        okursoProxy = OKursoProxy('Pablo', '1234')
        responseProxy = okursoProxy.makePurchase(
            idCompra, formaDePagamento, precoVenda, codCupom, codCurso, comprador)

        return responseProxy

    @staticmethod
    def getNextIDCompra():
        okursoProxy = OKursoProxy('Pablo', '1234')
        return okursoProxy.nextIdCompra()

    @staticmethod
    def efetuarLogin(email, senha):
        okursoProxy = OKursoProxy('Pablo', '1234')
        responseProxy = okursoProxy.login(email, senha)

        if type(responseProxy) == str:
            return responseProxy
        else:
            rows = responseProxy
            result = []
            keys = ['nome', 'email', 'cpf', 'senha']
            print(responseProxy)
            for row in rows:
                result.append(dict(zip(keys, row)))

            return result  # json.dumps(result)
