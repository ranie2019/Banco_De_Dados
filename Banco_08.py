# importando a biblioteca PyMysql
import pymysql

# conexao com o servidor
con = pymysql.connect(
    host = 'localhost',
    user =  'root',
    passwd = '',
    database = 'bbt'
)

# execucao de comando
cursor = con.cursor()

# instrucoes SQL

com_sql = 'INSERT INTO personagens(NOME, profissão) VALUES (%s, %s)'
valor = [
    ('Sheldon', 'Fisico Teorico'),
    ('Leonard', 'Fisico Experimental'),
    ('Bernadette', 'Microbiologista'),
    ('Amy', 'Neurobiologista'),
    ('Penny', 'Representante de vendas farmacêuticas'),
    ('howard', 'Engenharia aeroespacial'),
    ('Rajesh', 'Astrofísica'),

]
cursor.executemany(com_sql, valor)

con.commit()
print(cursor.rowcount,'inserido com sucesso')