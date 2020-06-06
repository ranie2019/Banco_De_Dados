# importando a biblioteca PyMysql
import pymysql

# criando a conexao com o web
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'bbt'
)

cursor = conexao.cursor()
cursor.execute('show tables')

# estrutura de repeticao (loop for
for x in cursor:
    print(x)