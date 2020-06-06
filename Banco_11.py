# importa biblioteca pymysql
import pymysql

# conecao com o servidor local
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'bbt'
)

cursor = conexao.cursor()

#comando e execucao de instrucoes
con_sql = 'update personagens set profissão = "baba"'

cursor.execute(con_sql)
conexao.commit()
print(cursor.rowcount,'tabela modificada e gravada')
