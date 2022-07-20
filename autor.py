from utils import write_json, write_json, is_existe_autor, get_json


def cadastrar_autor(data, nome_completo):
    if is_existe_autor(data, nome_completo):
        print("Autor ja cadastrado!")
        return data
    data["autor"].append(
        {
            "id": len(data["autor"]) + 1,
            "nome_completo": nome_completo,
            "is_active": True,
        }
    )
    write_json("data.json", data)
    print("Autor cadastrado com sucesso!")
    return data["autor"][-1]["id"]


def atualizar_autor(data, nome, novo_nome, is_active=True):
    for i in data["autor"]:
        if i["nome_completo"] == nome and i["is_active"] == True:
            i["nome_completo"] = novo_nome
            i["is_active"] = is_active
            write_json("data.json", data)
            print("autor atualizado com sucesso!")
            return data
    print("não encontrado!")
    return False


def apagar_autor(data, nome):
    atualizar_autor(data, nome, nome, False)
    return data


def listar_autor(data, is_active=True):
    print(f'{"ID":<8}{"NOME":^20}')
    print("-" * 50)
    for i in data["autor"]:
        if i["is_active"] == is_active:
            print(f"#{i['id']:^4} {i['nome_completo']:<20}")
            print("-" * 50)

    return data


def menu_autor(data):
    print("1 - Cadastrar Autor")
    print("2 - Listar Autores")
    print("3 - Alterar Autor")
    print("4 - Excluir Autor")
    print("5 - Voltar")
    try:
        opcao = input("Digite a opção desejada: ")
        opcao = int(opcao)
    except ValueError:
        print("Opção inválida!")
        return menu_autor(get_json("data.json"))

    if opcao == 1:
        print("Cadastrar Autor")
        nome = input("Digite o nome do autor: ")
        cadastrar_autor(data, nome)
    elif opcao == 2:
        print("Listar Autores")
        listar_autor(data)
    elif opcao == 3:
        print("Alterar Autor")
        nome = input("Digite o nome do autor a ser alterado: ")
        novo_nome = input("Digite o novo nome do autor: ")
        atualizar_autor(data, nome, novo_nome)
    elif opcao == 4:
        print("Excluir Autor")
        nome = input("Digite o nome do autor a ser excluído: ")
        apagar_autor(data, nome)
    elif opcao == 5:
        print("Voltar")
        return data

    return menu_autor(get_json("data.json"))


if __name__ == "__main__":
    pass
    # from faker import Faker
    # fake = Faker()
    # for i in range(10):
    #     cadastrar_autor(get_json("data.json"), fake.name())
