import json
from rest_framework import serializers
from .MySqlProxy import *

class ProgramacaoSerializer(serializers.Serializer):
    
    
    @staticmethod
    def serializerCourses(categoria):        # converter os dados do curso de programacao para JSON
        
        okursoProxy = OKursoProxy('Pablo', '1234')        
        responseProxy = okursoProxy.buscarCursos(categoria)
        
        print(categoria)
        
        if type(responseProxy) == str:
            return responseProxy
        else:
            rows = responseProxy
            result = []
            keys = ['nomeCurso','idCurso','autor','descricao','valor','categoria']

            for row in rows:            
                result.append(dict(zip(keys, row)))              

            return result #json.dumps(result) 
    