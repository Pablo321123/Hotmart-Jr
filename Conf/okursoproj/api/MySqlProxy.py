import decimal
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

    def getAllCourses(self, cursor, comando):
        cursor.execute(comando)
        return cursor.fetchall()

    def getCourses(self, cursor, cpf):
        cursor.execute(
            f"SELECT co.comprador, cu.idCurso, cu.nomeCurso, cu.duracao, cu.categoria, cu.descricao, cu.autor FROM COMPRA as co JOIN Curso as cu ON co.codCurso = cu.idCurso WHERE co.comprador = {cpf}")
        return cursor.fetchall()

    def insertUsuario(self, cursor, comando):
        cursor.execute(comando)

    def deleteUsuario(self, cursor, pk):
        cursor.execute(f"DELETE FROM usuario WHERE cpf = '{pk}'")

    def makePurchase(self, cursor, idCompra, formaDePagamento, precoVenda, codCupom: str, codCurso, comprador):
        if codCupom == "":
            cursor.execute(
                f"INSERT INTO Compra(idCompra, formaDePagamento, precoVenda, codCupom, codCurso, comprador) VALUES ({idCompra},'{formaDePagamento}', {precoVenda}, null, {codCurso}, {comprador})")
        else:
            cursor.execute(
                f"INSERT INTO Compra(idCompra, formaDePagamento, precoVenda, codCupom, codCurso, comprador) VALUES ({idCompra},'{formaDePagamento}', {precoVenda}, '{codCupom}', {codCurso}, {comprador})")

    def getModules(self, cursor, idCurso):
        cursor.execute(f"SELECT * FROM Modulo WHERE codCurso = {idCurso};")
        return cursor.fetchall()

    def getClass(self, cursor, idCurso, idModulo):
        cursor.execute(
            f"SELECT * FROM AULA as a JOIN modulo as m ON a.codModulo = m.idModulo JOIN curso as c ON c.idCurso = m.codCurso WHERE a.codModulo = {idModulo} AND c.idCurso = {idCurso};")
        return cursor.fetchall()

    def login(self, cursor, email, senha):
        cursor.execute(
            f"SELECT * FROM Usuario WHERE email = '{email}' AND senha = '{senha}'")
        return cursor.fetchall()


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

    def buscarTodosCursos(self, categoria):
        try:
            if self.isPermission():
                if categoria == "":                    
                    tuple = super().getAllCourses(self.dbCursor,
                                                  f"SELECT * FROM Curso")
                else:
                    tuple = super().getAllCourses(self.dbCursor,
                                                  f"SELECT * FROM Curso WHERE categoria = '{categoria}'")
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
                return True

            except Exception as e:
                print(f'{RED}{e}{RESET}')
                return False

    def deleteUsuario(self, pk):
        if self.isPermission():
            try:
                super().deleteUsuario(self.dbCursor, pk)
                print(f'{CYAN}Usuario com cpf {pk} deletado com sucesso!{RESET}')
            except Exception as e:
                print(f'{RED}{e}{RESET}')

    def makePurchase(self, idCompra, formaDePagamento, precoVenda, codCupom, codCurso, comprador):
        if self.isPermission():
            super().makePurchase(self.dbCursor, idCompra, formaDePagamento,
                                 self.calcOff(codCupom, precoVenda), codCupom, codCurso, comprador)
            return True

        return False

    # calcula o total do desconto no valor da compra
    def calcOff(self, cupom, valor):
        if self.isPermission():
            if cupom == "":
                return valor
            else:
                self.dbCursor.execute(
                    f"SELECT porcentagem FROM cupom WHERE idCupom = '{cupom}'")
                row = self.dbCursor.fetchone()
                valTotal = float(valor) * float(1 - (row[0]/100))
                return valTotal

    def nextIdCompra(self):
        if self.isPermission():
            self.dbCursor.execute(
                'SELECT MAX(idCompra) as idCompra FROM COMPRA')
            row = self.dbCursor.fetchone()
            return row[0] + 1

    def getCourses(self, cpf):
        return super().getCourses(self.dbCursor, cpf)

    def getModules(self, idCurso):
        if self.isPermission():
            return super().getModules(self.dbCursor, idCurso)

    def getClass(self, idCurso, idModulo):
        if self.isPermission():
            return super().getClass(self.dbCursor, idCurso, idModulo)

    def login(self, email, senha):
        if self.isPermission():
            return super().login(self.dbCursor, email, senha)
