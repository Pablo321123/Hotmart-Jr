import mysql.connector as mc


class DbPessoa:
    def __init__(self) -> None:
        self.userConnecteds = 45

    def getConnections(self) -> int:
        print(self.userConnecteds)
    
    def getUsuarios(self, listUsuarios) -> int:
         for r in listUsuarios:
            print(r)


class PessoaProxy(DbPessoa):
    def __init__(self, userName, userKey) -> None:
        super().__init__()
        self.user = 'root'
        self.password = 'toor'
        self.host = 'localhost'
        self.database = 'db_teste'
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
            print('Banco de dados conectado!')            

    def executeQuery(self, text):
        if self.isPermission():
            if self.isBdConnected():
                self.dbCursor = self.dbConnection.cursor()
                self.dbCursor.execute(text)
                print('Query realizada com sucesso!')

    def getUsuarios(self):
        if self.isPermission():
            super().getUsuarios(self.dbCursor)
            self.dbCursor.close()
        
    def getConnections(self):
        if self.isPermission():
            super().getConnections()

    def closeDB(self):
        self.dbConnection.close()
        


proxyTeste = PessoaProxy(userName='Pablo', userKey='1234')
proxyTeste.executeQuery('SELECT * FROM pessoas;')
proxyTeste.getUsuarios()
proxyTeste.getConnections()
proxyTeste.closeDB()
