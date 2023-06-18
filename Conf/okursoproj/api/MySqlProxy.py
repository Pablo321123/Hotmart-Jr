import mysql.connector as mc
from django.db import connection

RED = "\033[1;31m"
GREEN = "\033[0;32m"
CYAN = "\033[1;36m"
RESET = "\033[0;0m"


class DbPessoa:
    def __init__(self) -> None:
        self.userConnecteds = 45

    def getResult(self, listUsuarios) -> int:
        for r in listUsuarios:
            print(r)

    def getCourses(self, comando, cursor):
        cursor.execute(comando)
        return cursor.fetchall()

    def insertUsuario(self, cursor, comando):
        cursor.execute(comando)

    def deleteUsuario(self, cursor, pk):        
            cursor.execute(f"DELETE FROM usuario WHERE cpf = '{pk}'")


class OKursoProxy(DbPessoa):
    def __init__(self, userName, userKey) -> None:
        super().__init__()
        self.dbConnection = connection
        self.dbCursor = connection.cursor()
        self.userName = userName
        self.userKey = userKey

    def isPermission(self):
        return self.userName == 'Pablo' and self.userKey == '1234'

    def executeQuery(self, text):
        if self.isPermission():
            if self.isBdConnected():
                self.dbCursor.execute(text)
                super().getResult(self.dbCursor)   
                print(GREEN + 'Query realizada com sucesso!' + RESET)      

    def buscarCursos(self, categoria):
        try:
            if self.isPermission():
                tuple = super().getCourses(f"SELECT * FROM Curso WHERE categoria = '{categoria}';", self.dbCursor)
                return tuple
        except Exception as e:
            return f"{RED}{e}{RESET}"

    def insertUsuario(self, nome, email, cpf, senha):
        if self.isPermission():
            # self.dbCursor = self.dbConnection.cursor()
            try:
                super().insertUsuario(self.dbCursor,
                                      f"insert into Usuario(nome,email,cpf,senha) values ('{nome}', '{email}', {cpf}, '{senha}');")
                print(f'{CYAN}Usuario {nome} cadastrado com sucesso!{RESET}')
            except Exception as e:
                print(f'{RED}{e}{RESET}')

    def deleteUsuario(self, pk):
        if self.isPermission():
            try:
                super().deleteUsuario(self.dbCursor, pk)
                print(f'{CYAN}Usuario com cpf {pk} deletado com sucesso!{RESET}')
            except Exception as e:
                print(f'{RED}{e}{RESET}')

