from utils import write_json, write_json, is_existe_cliente, get_json


def cadastar_cliente(data, matricula, nome, email, telefone, quant_possivel=3):
    if is_existe_cliente(data, matricula):
        print("Cliente ja cadastrado!")
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
    for i in data["cliente"]:
        if i["is_active"] == is_active:
            print(i["id"], i["matricula"], i["nome"], i["email"], i["telefone"])
    return data


def menu_socios():
    print("1 - Cadastrar Sócio")
    print("2 - Listar Sócios")
    print("3 - Alterar Sócio")
    print("4 - Excluir Sócio")
    print("5 - Voltar")
    opcao = int(input("Digite a opção desejada: "))
    return opcao


if __name__ == "__main__":
    # listar_cliente(get_json('data.json'))
    # atualizar_cliente(data=get_json('data.json'), matricula=7786722, nome='João', email='obowman@example.org', telefone='+5511999999999')
    # apagar_cliente(data=get_json('data.json'), matricula=7786722)
    cadastar_cliente(
        get_json("data.json"),
        "xxx",
        "852147",
        "tes@email.com",
        "8555555",
        quant_possivel=3,
    )
