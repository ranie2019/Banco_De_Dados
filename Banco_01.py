# importando a biblioteca PyMysql
import pymysql

# criando a conexao com o servidor
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)
cursor = conexao.cursor()
cursor.execute('CREATE DATABASES bbt')
