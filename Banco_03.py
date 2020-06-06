# importando a biblioteca PyMysql
import pymysql

# criando a conexao com o web
con = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'bbt'
)
# execucao de comandos

cursor = con.cursor()
cursor.execute('create table personagens(id int auto_increment primary key, Nome VARCHAR(255), profissão VARCHAR(255))')

for x in cursor:
    print(x)