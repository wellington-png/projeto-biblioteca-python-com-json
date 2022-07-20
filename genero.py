from utils import write_json, write_json, get_json, is_existe_genero


def cadastar_genero(data, nome):
    if is_existe_genero(data, nome):
        print("Genero ja cadastrado!")
        return data

    data["genero"].append(
        {"id": len(data["genero"]) + 1, "nome": nome, "is_active": True}
    )
    write_json("data.json", data)
    print("Gênero cadastrado com sucesso!")
    return data["genero"][-1]["id"]


def atualizar_genero(data, nome, novo_nome, is_active=True):
    for i in data["genero"]:
        if i["nome"] == nome and i["is_active"] == True:
            i["nome"] = novo_nome
            i["is_active"] = is_active
            write_json("data.json", data)
            print("Operação realizada com com sucesso!")
            return data
    print("Gênero não encontrado!")
    return False


def apagar_genero(data, nome):
    atualizar_genero(data, nome, nome, False)
    return data


def listar_genero(data, is_active=True):
    print(f'{"ID":<8}{"NOME":^20}')
    print("-" * 50)
    for i in data["genero"]:
        if i["is_active"] == is_active:
            print(f"#{i['id']:^4} | {i['nome']:<40}")
            print("-" * 50)
    print("\n")
    return data


def menu_genero(data):
    print("1 - Cadastrar Gênero")
    print("2 - Listar Gêneros")
    print("3 - Alterar Gênero")
    print("4 - Excluir Gênero")
    print("5 - Voltar")

    try:
        opcao = input("Digite a opção desejada: ")
        opcao = int(opcao)
    except ValueError:
        print("Opção inválida!")
        return menu_genero(get_json("data.json"))
    
    
    if opcao == 1:
        print("Cadastrar Gênero")
        nome = input("Digite o nome do gênero: ")
        cadastar_genero(data, nome)

    elif opcao == 2:
        print("Listar Gêneros")
        listar_genero(data)
    elif opcao == 3:
        print("Alterar Gênero")
        nome = input("Digite o nome do gênero a ser alterado: ")
        novo_nome = input("Digite o novo nome do gênero: ")
        atualizar_genero(data, nome, novo_nome)
    elif opcao == 4:
        print("Excluir Gênero")
        nome = input("Digite o nome do gênero a ser excluído: ")
        apagar_genero(data, nome)
    elif opcao == 5:
        return data
    return menu_genero(get_json("data.json"))


if __name__ == "__main__":
    cadastar_genero(get_json("data.json"), "filme")
