# importando a biblioteca pymysql
import pymysql

#conexao com o servidor web
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'bbt'
)

cursor = conexao.cursor()

# comandos sql
con_sql = 'drop table homen'

cursor.execute(con_sql)
