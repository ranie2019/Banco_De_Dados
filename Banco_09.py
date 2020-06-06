# importando a biblioteca PyMysql
import pymysql

# conexao com o servidor
con = pymysql.connect(
    host = 'localhost',
    user =  'root',
    passwd = '',
    database = 'bbt'
)
cursor = con.cursor()
cursor.execute('select * from personagens ')

resultado = cursor.fetchall()

for x in resultado:
    print(x)