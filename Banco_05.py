# importando a biblioteca PyMysql
import pymysql

# criando a conexao com o web
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'bbt'
)
# execucao de comando
cursor = conexao.cursor()
cursor.execute('create table mulher(Nome VARCHAR(255), profissão VARCHAR(255))')

for x in cursor:
    print(x)