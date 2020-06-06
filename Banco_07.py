# importando a biblioteca PyMysql
import pymysql

# conexao local
con = pymysql.connect(
    host = 'localhost',
    user =  'root',
    passwd = '',
    database = 'bbt'
)

# execucao de comando
cursor = con.cursor()
cursor.execute('alter table homen add column id int auto_increment primary key')
