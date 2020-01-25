import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='teste'
)

cursor = conexao.cursor()
cursor.execute("INSERT INTO produto(nome,preco,quantidade) VALUES('Bolacha2',2.00,34)")
conexao.commit()


