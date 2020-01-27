import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='teste'
)


def insereProduto(nome, preco, quantidade):
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produto(nome, preco, quantidade) VALUES('{}',{},{})".format(nome, preco, quantidade))
    conexao.commit()


def deletaProduto(id):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produto WHERE idproduto = {}".format(id))
    conexao.commit()


def alteraNome(nome, ID):
    cursor = conexao.cursor()
    cursor.execute("UPDATE produto SET nome = {} WHERE = {}".format(nome, ID))
    conexao.commit()


def alteraPreco(preco, id):
    cursor = conexao.cursor()
    cursor.execute("UPDATE produto SET preco = {} WHERE idproduto = {}".format(preco, id))
    conexao.commit()


def alteraQtd(qtd, id):
    cursor = conexao.cursor()
    cursor.execute("UPDATE produto SET quantidade = {} WHERE idproduto = {}".format(qtd, id))
    conexao.commit()


def listarTodos():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto")
    return cursor.fetchall()