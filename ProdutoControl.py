import ProdutoModel


def menuInicial():
    print("Cadastro De Produtos\n\n")
    print("Digite 1 para listar os produtos cadastrados")
    print("Digite 2 para cadastrar um novo produto")
    print("Digite 3 para editar um produto específico")
    print("Digite 0 para Sair")
    return input("\n\n==>")


def novoCadastro():
    validaNome = 1
    while validaNome == 1:
        nome = input("Digite 0 para sair\n\nDigite o nome do produto\n\n==>")
        validaNome = ProdutoModel.verificaExistencia(nome)
        if validaNome < 1:

            preco = input("Digite o preço  do produto\n\n==>")
            quantidade = input("Digite a quantidade de unidades disponíveis\n\n==>")
            ProdutoModel.insereProduto(nome, preco, quantidade)
            if ProdutoModel.verificaExistencia(nome) < 1:
                print("Ocorreu um erro ao cadastrar.\n")
            else:
                print("Cadastro Realizado com sucesso!!!\n")
        elif nome == 0:
            validaNome = 0
        else:
            print("Produto Já Cadastrado!!!!!\n\n\n")


def menuEditarProduto():
    print(ProdutoModel.listarTodos())
    print("Edicao de Produtos\n\n")
    print("Digite 1 para editar um nome passando Id")
    print("Digite 2 para editar um preço passando Id")
    print("Digite 3 para editar uma quantidade passando Id")
    print("Digite 0 para Sair")
    return input("\n\n==>")



def editarNome():
    id = input("Digite o Id do produto desejado\n\n")
    nome = ProdutoModel.verificaNome(id)

    print(nome)
