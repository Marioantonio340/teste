import ProdutoModel


def menuInicial():
    print("Cadastro De Produtos\n\n")
    print("Digite 1 para listar os produtos cadastrados")
    print("Digite 2 para cadastrar um novo produto")
    print("Digite 3 para editar um produto específico")
    print("Digite 4 para pesquisar por nome")
    print("Digite 5 para usar filtros em valor e quantidade")
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
                print(
                    "---------------------------------------------------------------------------------------\nOcorreu um erro ao cadastrar.\n---------------------------------------------------------------------------------------")
            else:
                print(
                    "---------------------------------------------------------------------------------------\nCadastro Realizado com sucesso!!!\n---------------------------------------------------------------------------------------")
        elif nome == 0:
            validaNome = 0
        else:
            print(
                "---------------------------------------------------------------------------------------\nProduto Já Cadastrado!!!!!\n---------------------------------------------------------------------------------------")


def menuEditarProduto():
    print(ProdutoModel.listarTodos())
    print("Edicao de Produtos\n\n")
    print("Digite 1 para editar um nome passando Id")
    print("Digite 2 para editar um preço passando Id")
    print("Digite 3 para editar uma quantidade passando Id")
    print("Digite 4 para deletar um produto passando Id")
    print("Digite 0 para Sair")
    return input("\n\n==>")


def editarNome():
    i = "n"
    while (i == "n") or (i == "N"):
        id = input("Digite o Id do produto desejado\n\n")
        nome = ProdutoModel.verificaNome(id)
        print("Deseja editar {}?".format(nome))
        i = input("s/sim n/não\n\n==>")
        if (i == 's') or (i == 'S'):
            novoNome = input("Digite o novo nome\n\n==>")
            validaNome = ProdutoModel.verificaExistencia(novoNome)
            if validaNome < 1:
                ProdutoModel.alteraNome(novoNome, id)
                print(
                    "---------------------------------------------------------------------------------------\nAlterado com sucesso!!!\n---------------------------------------------------------------------------------------")
            else:
                print(
                    "---------------------------------------------------------------------------------------\nProduto Já Cadastrado!!!!!\n---------------------------------------------------------------------------------------")
        elif (i != 'n') and (i != 'N'):
            print(
                "---------------------------------------------------------------------------------------\nComando Inválido!!!!!\n---------------------------------------------------------------------------------------")
            i = 'n'


def editarPreco():
    i = "n"
    while (i == "n") or (i == "N"):
        id = input("Digite o Id do produto desejado\n\n")
        nome = ProdutoModel.verificaNome(id)
        print("Deseja editar o preco de {}?".format(nome))
        i = input("s/sim n/não\n\n==>")
        if (i == 's') or (i == 'S'):
            novoValor = input("Digite o novo preco\n\n==>")
            ProdutoModel.alteraPreco(novoValor, id)
            print(
                "---------------------------------------------------------------------------------------\nAlterado com sucesso!!!\n---------------------------------------------------------------------------------------")
        elif (i != 'n') and (i != 'N'):
            print(
                "---------------------------------------------------------------------------------------\nComando Inválido!!!!!\n---------------------------------------------------------------------------------------")
            i = 'n'


def editarQuantidade():
    i = "n"
    while (i == "n") or (i == "N"):
        id = input("Digite o Id do produto desejado\n\n")
        nome = ProdutoModel.verificaNome(id)
        print("Deseja editar a quantidade de {}?".format(nome))
        i = input("s/sim n/não\n\n==>")
        if (i == 's') or (i == 'S'):
            novaQtd = input("Digite a nova quantidade\n\n==>")
            ProdutoModel.alteraQtd(novaQtd, id)
            print(
                "---------------------------------------------------------------------------------------\nAlterado com sucesso!!!\n---------------------------------------------------------------------------------------")
        elif (i != 'n') and (i != 'N'):
            print(
                "---------------------------------------------------------------------------------------\nComando Inválido!!!!!\n---------------------------------------------------------------------------------------")
            i = 'n'


def deletarProduto():
    i = "n"
    while (i == "n") or (i == "N"):
        id = input("Digite o Id do produto desejado\n\n")
        nome = ProdutoModel.verificaNome(id)
        print("Deseja deletar {}?".format(nome))
        i = input("s/sim n/não\n\n==>")
        if (i == 's') or (i == 'S'):
            ProdutoModel.deletaProduto(id)
            print(
                "---------------------------------------------------------------------------------------\nDeletado com sucesso!!!\n---------------------------------------------------------------------------------------")
        elif (i != 'n') and (i != 'N'):
            print(
                "---------------------------------------------------------------------------------------\nComando Inválido!!!!!\n---------------------------------------------------------------------------------------")
            i = 'n'


def pesquisa():
    nome = input("Digite o que deseja pesquisar")
    ProdutoModel.pesquisaNome(nome)


def filtros():
    vfiltro = 0
    while vfiltro < 1:
        valor = input("Digite 1 para filtrar por preco\nDigite 2 para filtrar por quantidade\n\n==>")
        if (valor != '1') and (valor != '2'):
            print(
                "---------------------------------------------------------------------------------------\nComando Inválido!!!!!\n---------------------------------------------------------------------------------------")
        else:
            vfiltro = 1

            pmenu = 0
            while pmenu < 1:

                opcaoMenu = menuFiltro()

                if opcaoMenu == '1':
                    ProdutoModel.filtroCrescente(valor)
                elif opcaoMenu == '2':
                    ProdutoModel.filtroDecrescente(valor)
                elif opcaoMenu == '3':
                    ProdutoModel.filtroMaior(valor, input("Digite o valor de X\n\n==>"))
                elif opcaoMenu == '4':
                    ProdutoModel.filtroMenor(valor, input("Digite o valor de X\n\n==>"))
                elif opcaoMenu == '5':
                    ProdutoModel.filtroValoresEntre(valor, input("Digite o valor de X\n\n==>"), input("Digite o valor de Y\n\n==>"))
                elif opcaoMenu == '0':
                    pmenu = 1
                else:
                    print("---------------------------------------------------------------------------------------\nComando Inválido!!!!!\n---------------------------------------------------------------------------------------")
                    pmenu = 0



def menuFiltro():
    print("Digite 1 para Filtrar em ordem crescente")
    print("Digite 2 para Filtrar em ordem decrescente")
    print("Digite 3 para Filtrar valores maiores que X")
    print("Digite 4 para Filtrar valores menores que X")
    print("Digite 5 para Filtrar valores entre X e Y")
    print("Digite 0 para Sair")
    return input("\n\n==>")
