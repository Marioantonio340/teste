import ProdutoModel
import Menus

pmenu = 0
while pmenu < 1:
    pmenu = 1
    opcaoMenu = Menus.menuInicial()

    if opcaoMenu == '1':
        print(ProdutoModel.listarTodos())
    if opcaoMenu == '2':
            print(ProdutoModel.listarTodos())
    if opcaoMenu == '3':
        print(ProdutoModel.listarTodos())
    else:
        print("Comando Inválido!")
        pmenu = 0
