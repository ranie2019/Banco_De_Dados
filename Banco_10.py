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

# comando de execucao banco de dados

con_sql = 'select * FROM personagens order by nome desc'
cursor.execute(con_sql)

resultado = cursor.fetchall()

for x in resultado:
    print(x)