import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='teste'
)


def insereProduto(nome, preco, quantidade):  # insere
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produto(nome, preco, quantidade) VALUES('{}',{},{})".format(nome, preco, quantidade))
    conexao.commit()


def deletaProduto(id):  # deleta
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produto WHERE idproduto = {}".format(id))
    conexao.commit()


def alteraNome(nome, ID):  # altera o nome
    cursor = conexao.cursor()
    cursor.execute("UPDATE produto SET nome = '{}' WHERE idproduto = {}".format(nome, ID))
    conexao.commit()


def alteraPreco(preco, id):  # altera o preco
    cursor = conexao.cursor()
    cursor.execute("UPDATE produto SET preco = {} WHERE idproduto = {}".format(preco, id))
    conexao.commit()


def alteraQtd(qtd, id):  # altera a quantidade
    cursor = conexao.cursor()
    cursor.execute("UPDATE produto SET quantidade = {} WHERE idproduto = {}".format(qtd, id))
    conexao.commit()


def listarTodos():  # Lista todos os produtos em formato de tabela
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto")
    result = cursor.fetchall()
    for produto in result:
        print(
            "Id:{}  // Nome:{}  //  Preço:{}  //  Quantidade:{}\n---------------------------------------------------------------------------------------".format(
                produto[0], produto[1], produto[2], produto[3]))


def verificaExistencia(nome1):  # Verifica se o produto existe, se sim retorna 1
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto WHERE nome = '{}'".format(nome1))
    conexao.commit()
    return cursor.rowcount


def verificaNome(id):  # verifica se o nome existe, se sim retorna o mesmo
    cursor = conexao.cursor()
    cursor.execute("SELECT nome FROM produto WHERE idproduto = {}".format(id))
    rows = cursor.rowcount
    if rows == 0:
        print(
            "---------------------------------------------------------------------------------------\nO produto escolhido não existe!\n---------------------------------------------------------------------------------------")
        return
    else:
        result = cursor.fetchone()
        return result[0]


def pesquisaNome(nome):  # realiza uma pesquisa por strig e lista em formato de tabela
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto WHERE nome LIKE '%{}%'".format(nome))
    result = cursor.fetchall()
    for produto in result:
        print(
            "Id:{}  // Nome:{}  //  Preço:{}  //  Quantidade:{}\n---------------------------------------------------------------------------------------".format(
                produto[0], produto[1], produto[2], produto[3]))


def filtroCrescente(valor):
    if valor == '2':
        valor = 'quantidade'
    else:
        valor = 'preco'

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto ORDER BY {} ASC".format(valor))
    result = cursor.fetchall()
    for produto in result:
        print(
            "Id:{}  // Nome:{}  //  Preço:{}  //  Quantidade:{}\n---------------------------------------------------------------------------------------".format(
                produto[0], produto[1], produto[2], produto[3]))



def filtroDecrescente(valor):
    if valor == '2':
        valor = 'quantidade'
    else:
        valor = 'preco'

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto ORDER BY {} DESC".format(valor))
    result = cursor.fetchall()
    for produto in result:
        print(
            "Id:{}  // Nome:{}  //  Preço:{}  //  Quantidade:{}\n---------------------------------------------------------------------------------------".format(
                produto[0], produto[1], produto[2], produto[3]))


def filtroMaior(valor, valor2):
    if valor == '2':
        valor = 'quantidade'
    else:
        valor = 'preco'

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto  WHERE {0} > {1} ORDER BY {0} ASC;".format(valor, valor2))
    result = cursor.fetchall()
    for produto in result:
        print(
            "Id:{}  // Nome:{}  //  Preço:{}  //  Quantidade:{}\n---------------------------------------------------------------------------------------".format(
                produto[0], produto[1], produto[2], produto[3]))


def filtroMenor(valor, valor2):
    if valor == '2':
        valor = 'quantidade'
    else:
        valor = 'preco'

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto  WHERE {0} < {1} ORDER BY {0} DESC;".format(valor, valor2))
    result = cursor.fetchall()
    for produto in result:
        print(
            "Id:{}  // Nome:{}  //  Preço:{}  //  Quantidade:{}\n---------------------------------------------------------------------------------------".format(
                produto[0], produto[1], produto[2], produto[3]))



def filtroValoresEntre(valor, valor2, valor3):
    if valor == '2':
        valor = 'quantidade'
    else:
        valor = 'preco'

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto  WHERE {0} BETWEEN {1} AND {2} ORDER BY {0} ASC;".format(valor, valor2, valor3))
    result = cursor.fetchall()
    for produto in result:
        print(
            "Id:{}  // Nome:{}  //  Preço:{}  //  Quantidade:{}\n---------------------------------------------------------------------------------------".format(
                produto[0], produto[1], produto[2], produto[3]))