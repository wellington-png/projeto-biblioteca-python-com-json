from utils import write_json, get_json, write_json
import livro
import genero
import cliente as socio
import autor as a
import emprestimo

data = get_json('data.json')


def menu():
    print('1 - Livros')
    print('2 - Gêneros')
    print('3 - Sócios')
    print('4 - Autores')
    print('5 - Emprestimos')
    print('6 - Sair')
    opcao = int(input('Digite a opção desejada: '))
    return opcao

while True:
    opcao = menu()

    if opcao == 1:
        opcao = livro.menu_livro()
        if opcao == 1:
            print('Cadastrar Livro')
            titulo = input('Digite o titulo do livro: ')
            autor = input('Digite o nome do autor: ')
            genero = input('Digite o nome do gênero: ')
            ano = int(input('Digite o ano do livro: '))
            quantidade = int(input('Digite a quantidade de livros: '))
            disponivel = int(input('Digite a quantidade de livros disponíveis: '))
            codigo = input('Digite o código do livro: ')
            livro.cadastrar_livro(data, titulo, autor, genero, quantidade, disponivel, ano, codigo)
        elif opcao == 2:
            print('Listar Livros')
            livro.listar_livro(data)
        elif opcao == 3:
            print('Alterar Livro')
            codigo = input('Digite o código do livro: ')
            titulo = input('Digite o titulo do livro: ')
            autor = input('Digite o nome do autor: ')
            genero = input('Digite o nome do gênero: ')
            ano = int(input('Digite o ano do livro: '))
            quantidade = int(input('Digite a quantidade de livros: '))
            disponivel = int(input('Digite a quantidade de livros disponíveis: '))
            livro.atualizar_livro(data, codigo, titulo=None, autor=None, genero=None, quantidade=None, disponivel=None, ano=None)
        elif opcao == 4:
            print('Excluir Livro')
            codigo = input('Digite o código do livro: ')
            livro.apagar_livro(data, codigo)
        elif opcao == 5:
            print('Voltar')
  
    elif opcao == 2:
        opcao = genero.menu_genero()
        if opcao == 1:
            print('Cadastrar Gênero')
            nome = input('Digite o nome do gênero: ')
            genero.cadastar_genero(data, nome)
             
        elif opcao == 2:
            print('Listar Gêneros')
            genero.listar_genero(data)
        elif opcao == 3:
            print('Alterar Gênero')
            nome = input('Digite o nome do gênero a ser alterado: ')
            novo_nome = input('Digite o novo nome do gênero: ')
            genero.atualizar_genero(data, nome, novo_nome)
        elif opcao == 4:
            print('Excluir Gênero')
            nome = input('Digite o nome do gênero a ser excluído: ')
            genero.apagar_genero(data, nome)
        elif opcao == 5:
            print('Voltar')

    elif opcao == 3:
        opcao = socio.menu_socios()
        if opcao == 1:
            print('Cadastrar Sócio')
            nome = input('Digite o nome do sócio: ')
            matricula = input('Digite a matricula do sócio: ')
            email = input('Digite o email do sócio: ')
            telefone = input('Digite o telefone do sócio: ')
            quantidade = int(input('Digite a quantidade de livros que o sócio pode pegar: '))
            socio.cadastar_cliente(data, matricula, nome, email, telefone, quant_possivel=quantidade)
        elif opcao == 2:
            print('Listar Sócios')
            socio.listar_cliente(data)
        elif opcao == 3:
            print('Alterar Sócio')
            matricula = input('Digite a matricula do sócio a ser alterado: ')
            nome = input('Digite o nome do sócio a ser alterado: ')
            email = input('Digite o email do sócio a ser alterado: ')
            telefone = input('Digite o telefone do sócio a ser alterado: ')
            quantidade = int(input('Digite a quantidade de livros que o sócio pode pegar: '))
            socio.atualizar_cliente(data, matricula, nome=nome, email=email, telefone=telefone, quant_possivel=quantidade)
        elif opcao == 4:
            print('Excluir Sócio')
            matricula = input('Digite a matricula do sócio a ser excluído: ')
            socio.apagar_cliente(data, matricula)
        elif opcao == 5:
            print('Voltar')

    elif opcao == 4:
        opcao = a.menu_autor()
        if opcao == 1:
            print('Cadastrar Autor')
            nome = input('Digite o nome do autor: ')
            a.cadastrar_autor(data, nome)
        elif opcao == 2:
            print('Listar Autores')
            a.listar_autor(data)
        elif opcao == 3:
            print('Alterar Autor')
            nome = input('Digite o nome do autor a ser alterado: ')
            novo_nome = input('Digite o novo nome do autor: ')
            a.atualizar_autor(data, nome, novo_nome)
        elif opcao == 4:
            print('Excluir Autor')
            nome = input('Digite o nome do autor a ser excluído: ')
            a.apagar_autor(data, nome)
        elif opcao == 5:
            print('Voltar')
            menu()

    elif opcao == 5:
        opcao = emprestimo.menu_emprestimo()
        if opcao == 1:
            print('Emprestar Livro')
        elif opcao == 2:
            print('Devolver Livro')
        elif opcao == 3:
            print('Listar Emprestimos')
        elif opcao == 4:
            print('Voltar')
    elif opcao == 6:
        print('Saindo...')
        break

