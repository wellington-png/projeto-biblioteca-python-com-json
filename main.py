from utils import get_json, write_json
from livro import menu_livro
from genero import menu_genero
from cliente import menu_socios
from autor import menu_autor
from emprestimo import menu_emprestimo
data = get_json("data.json")


def menu():
    print("1 - Livros")
    print("2 - Gêneros")
    print("3 - Sócios")
    print("4 - Autores")
    print("5 - Emprestimos")
    print("6 - Sair")
    
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida!")
        return menu()
    return opcao


while True:
    opcao = menu()

    if opcao == 1:
        menu_livro(get_json("data.json"))

    elif opcao == 2:
        menu_genero(get_json("data.json"))

    elif opcao == 3:
        menu_socios(get_json("data.json"))

    elif opcao == 4:
        menu_autor(get_json("data.json"))

    elif opcao == 5:
        menu_emprestimo(get_json("data.json"))

    elif opcao == 6:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
        continue
