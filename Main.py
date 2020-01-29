import ProdutoModel
import ProdutoControl
ProdutoModel.verificaExistencia("marcos")
pmenu = 0
while pmenu < 1:

    opcaoMenu = ProdutoControl.menuInicial()

    if opcaoMenu == '1':
        print(ProdutoModel.listarTodos())
    elif opcaoMenu == '2':
        pCadastro = input("Deseja Cadastrar um novo produto?s/sim n/não\n\n==>")
        if (pCadastro == 's') or (pCadastro == 'S'):
            ProdutoControl.novoCadastro()
    elif opcaoMenu == '3':
        peditar = 0
        while peditar < 1:

            opcaoEditar = ProdutoControl.menuEditarProduto()

            if opcaoEditar == '1':
                ProdutoControl.editarNome()
            elif opcaoEditar == '2':
                ProdutoControl.editarPreco()
            elif opcaoEditar == '3':
                ProdutoControl.editarQuantidade()
            elif opcaoEditar == '4':
                ProdutoControl.deletarProduto()
            elif opcaoEditar == '0':
                peditar = 1
            else:
                print("---------------------------------------------------------------------------------------\nComando Inválido!!!!!\n---------------------------------------------------------------------------------------")
                peditar = 0
    elif opcaoMenu == '4':
        ProdutoControl.pesquisa()
    elif opcaoMenu == '5':
        ProdutoControl.filtros()
    elif opcaoMenu == '0':
        pmenu = 1
    else:
        print("---------------------------------------------------------------------------------------\nComando Inválido!!!!!\n---------------------------------------------------------------------------------------")
        pmenu = 0


