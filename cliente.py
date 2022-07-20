from utils import write_json, write_json, is_existe_cliente, get_json


def cadastar_cliente(data, matricula, nome, email, telefone, quant_possivel=3):
    if is_existe_cliente(data, matricula):
        print("Matricula inválida!")
        return data
    data["cliente"].append(
        {
            "id": len(data["cliente"]) + 1,
            "matricula": matricula,
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "is_active": True,
            "quant_possivel": quant_possivel,
        }
    )
    print("Sócio cadastrado com sucesso!")
    write_json("data.json", data)
    return data["cliente"][-1]


def atualizar_cliente(
    data,
    matricula,
    nome=None,
    email=None,
    telefone=None,
    is_active=True,
    quant_possivel=None,
):
    for i in data["cliente"]:
        if i["matricula"] == matricula and i["is_active"] == True:
            i["nome"] = nome if nome else i["nome"]
            i["email"] = email if email else i["email"]
            i["telefone"] = telefone if telefone else i["telefone"]
            i["is_active"] = is_active
            i["quant_possivel"] = (
                quant_possivel if quant_possivel else i["quant_possivel"]
            )
            write_json("data.json", data)
            print("Cliente atualizado com sucesso!")
            return data
    print("Cliente não encontrado!")
    return False


def apagar_cliente(data, matricula):
    atualizar_cliente(data, matricula=matricula, is_active=False)
    return data


def listar_cliente(data, is_active=True):
    print(
        f'{"ID":<4}{"MATRICULA":^12}{"NOME":^30}{"EMAIL":^30}{"TELEFONE":^15}{"QUANTIDADE":>15}'
    )
    print("-" * 110)
    for i in data["cliente"]:
        if i["is_active"] == is_active:
            print(
                f'{i["id"]:<4}{i["matricula"]:<15}{i["nome"]:<30}{i["email"]:<30}{i["telefone"]:<15}{i["quant_possivel"]:^8}'
            )
            print("-" * 110)

    return data


def socio_detalhes(data, matricula):
    for i in data["cliente"]:
        if i["matricula"] == matricula:
            print(
                f'{"ID":<4}{"MATRICULA":^12}{"NOME":^30}{"EMAIL":^30}{"TELEFONE":^15}{"QUANTIDADE":>15}'
            )
            print("-" * 110)
            print(
                f'{i["id"]:<4}{i["matricula"]:<15}{i["nome"]:<30}{i["email"]:<30}{i["telefone"]:<15}{i["quant_possivel"]:^8}'
            )
            print("-" * 110)
            return data
    print("Sócio não encontrado!")
    return False


def menu_socios(data):
    print("1 - Cadastrar Sócio")
    print("2 - Listar Sócios")
    print("3 - Detalhes do Sócio")
    print("4 - Alterar Sócio")
    print("5 - Excluir Sócio")
    print("6 - Voltar")
    
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida!")
        return menu_socios(get_json("data.json"))
    

    if opcao == 1:
        print("Cadastrar Sócio")
        nome = input("Digite o nome do sócio: ")
        matricula = input("Digite a matricula do sócio: ")
        email = input("Digite o email do sócio: ")
        telefone = input("Digite o telefone do sócio: ")
        quantidade = input("Digite a quantidade de livros que o sócio pode pegar: ")

        if quantidade.isdigit():
            quantidade = int(quantidade)
            cadastar_cliente(
                data, matricula, nome, email, telefone, quant_possivel=quantidade
            )
            socio_detalhes(data, matricula)
        else:
            print("Quantidade de livros deve ser um número!")
            return menu_socios(data)
    elif opcao == 2:
        print("Listar Sócios")
        listar_cliente(data)

    elif opcao == 3:
        print("Detalhes do Sócio")
        matricula = input("Digite a matricula do sócio: ")
        socio_detalhes(data, matricula)

    elif opcao == 4:
        print("Alterar Sócio")
        matricula = input("Digite a matricula do sócio a ser alterado: ")
        nome = input("Digite o nome do sócio a ser alterado: ")
        email = input("Digite o email do sócio a ser alterado: ")
        telefone = input("Digite o telefone do sócio a ser alterado: ")
        quantidade = input("Digite a quantidade de livros que o sócio pode pegar: ")

        if quantidade.isdigit():
            quantidade = int(quantidade)
            atualizar_cliente(
                data,
                matricula,
                nome,
                email,
                telefone,
                quant_possivel=quantidade,
            )
            socio_detalhes(data, matricula)
        else:
            print("Quantidade de livros deve ser um número!")

    elif opcao == 5:
        print("Excluir Sócio")
        matricula = input("Digite a matricula do sócio a ser excluído: ")
        apagar_cliente(data, matricula)
    elif opcao == 6:
        return data

    menu_socios(get_json("data.json"))


if __name__ == "__main__":
    listar_cliente(get_json("data.json"))
    # atualizar_cliente(data=get_json('data.json'), matricula=7786722, nome='João', email='obowman@example.org', telefone='+5511999999999')
    # apagar_cliente(data=get_json('data.json'), matricula=7786722)
    # cadastar_cliente(
    #     get_json("data.json"),
    #     "xxx",
    #     "852147",
    #     "tes@email.com",
    #     "8555555",
    #     quant_possivel=3,
    # )
