import mysql.connector as mc
import MySqlConnector

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

    def insertUsuario(self, cursor, comando):
        cursor.execute(comando)

    def deleteUsuario(self, cursor, pk):        
            cursor.execute(f"DELETE FROM usuario WHERE cpf = '{pk}'")


class PessoaProxy(DbPessoa):
    def __init__(self, userName, userKey) -> None:
        super().__init__()
        self.user = 'root'
        self.password = 'toor'
        self.host = 'localhost'
        self.database = 'okurso'
        self.userName = userName
        self.userKey = userKey
        self.dbConnection = None
        self.dbCursor = None
        self.connectDB()

    def isBdConnected(self) -> bool:
        return self.dbConnection.is_connected()

    def isPermission(self):
        return self.userName == 'Pablo' and self.userKey == '1234'

    def connectDB(self):
        self.dbConnection = mc.connect(user=self.user, password=self.password,
                                       host=self.host, database=self.database)

        if self.isBdConnected():
            print(GREEN + 'Banco de dados conectado!' + RESET)
            self.dbCursor = self.dbConnection.cursor()

    def executeQuery(self, text):
        if self.isPermission():
            if self.isBdConnected():
                self.dbCursor.execute(text)
                super().getResult(self.dbCursor)   
                print(GREEN + 'Query realizada com sucesso!' + RESET)      

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

    def closeDB(self):
        if self.isBdConnected():
            self.dbConnection.commit()
            self.dbConnection.close()
            self.dbCursor.close()
            print(GREEN + 'Banco de dados encerrado!' + RESET)
        else:
            print(CYAN + 'Não há conexões ativas do banco de dados!' + RESET)


proxyTeste = PessoaProxy(userName='Pablo', userKey='1234')
#proxyTeste.insertUsuario('Klay', 'klay@gmail.com', 12345678910, 'rasdlol2')
proxyTeste.executeQuery('SELECT * FROM usuario;')
proxyTeste.deleteUsuario(12345678910)
proxyTeste.closeDB()
