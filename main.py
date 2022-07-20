from utils import get_json, write_json
from livro import menu_livro
from genero import menu_genero
from cliente import menu_socios
from autor import menu_autor
from emprestimo import menu_emprestimo
data = get_json("data.json")


def menu():
    print(f'+{" Menu Principal ":-^28}+')
    print(f'|{" 1 ":<5}{" Livro ":<23}|')
    print(f'|{" 2 ":<5}{" Genero ":<23}|')
    print(f'|{" 3 ":<5}{" Socios ":<23}|')
    print(f'|{" 4 ":<5}{" Autor ":<23}|')
    print(f'|{" 5 ":<5}{" Emprestimo ":<23}|')
    print(f'|{" 6 ":<5}{" Sair ":<23}|')
    print(f'+{"-"*28}+')
    
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
