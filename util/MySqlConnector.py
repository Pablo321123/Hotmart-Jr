import mysql.connector as mc

connection = mc.connect(
    host='localhost', database='db_teste', user='root', password='toor')

if connection.is_connected():
    print("Conexão com banco de dados bem sucedida!")
    cursor = connection.cursor()
    
    text = 'SELECT * FROM pessoas;'
    cursor.execute(text)  
    for r in cursor:
        print(r)


cursor.close()
connection.close()
