from cliente import cadastar_cliente
from utils import (
    write_json,
    get_json,
    is_existe_livro,
    is_existe_cliente,
    pode_emprestar,
    ja_emprestou,
    estoque,
    datetime_to_str,
    str_to_datetime,
    soma_data,
    tem_livro_atrazado,
)
from datetime import datetime

data_atual = datetime_to_str(datetime.now())


def emprestar_livro(data, livro, cliente, dias_para_devolucao, devolvido=False):
    livro_id = is_existe_livro(data, livro)
    cliente_id = is_existe_cliente(data, cliente)
    if livro_id and cliente_id:
        prazo = datetime_to_str(
            soma_data(str_to_datetime(data_atual), dias_para_devolucao)
        )
        if ja_emprestou(data, cliente_id[1], livro_id[1]):
            if pode_emprestar(data, cliente) and estoque(data, livro):
                if tem_livro_atrazado(data, cliente_id[1]):
                    data["emprestimo"].append(
                        {
                            "id": len(data["emprestimo"]) + 1,
                            "livro": livro_id[1],
                            "cliente": cliente_id[1],
                            "data_emprestimo": data_atual,
                            "dias_devolucao": dias_para_devolucao,
                            "prazo": prazo,
                            "devolvido": devolvido,
                        }
                    )
                    t = livro_id[1] - 1
                    c = cliente_id[1] - 1
                    data["livro"][t]["disponivel"] -= 1
                    data["cliente"][c]["quant_possivel"] -= 1
                    write_json("data.json", data)
                    return data["emprestimo"][-1]
                else:
                    print("Cliente com livro atrasado")
            else:
                print("Cliente ou Livro não possui quantidade disponível")
                return False
        else:
            print("Você já emprestou esse livro!")
            return False
    else:
        print("Livro ou cliente não encontrado!")
        return False


def devolver_livro(data, cod_livro, matricula):
    livro_id = is_existe_livro(data, cod_livro)
    cliente_id = is_existe_cliente(data, matricula)
    if cliente_id and livro_id:
        for i in data["emprestimo"]:
            if (
                i["livro"] == livro_id[1]
                and i["cliente"] == cliente_id[1]
                and i["devolvido"] == False
            ):
                i["devolvido"] = True
                i["data_devolucao"] = datetime_to_str(datetime.now())
                t = i["livro"] - 1
                c = i["cliente"] - 1
                data["livro"][t]["disponivel"] += 1
                data["cliente"][c]["quant_possivel"] += 1
                write_json("data.json", data)
                print("Livro devolvido com sucesso!")
                return True
    print("Livro não encontrado!")
    return False


def renovar_emprestimo(data, matricula, cod_livro, dias):
    livro_id = is_existe_livro(data, cod_livro)
    cliente_id = is_existe_cliente(data, matricula)
    if cliente_id and livro_id:
        for i in data["emprestimo"]:
            if (
                i["livro"] == livro_id[1]
                and i["cliente"] == cliente_id[1]
                and i["devolvido"] == False
            ):
                i["data_devolucao"] = datetime_to_str(datetime.now())
                i["prazo"] = datetime_to_str(
                    soma_data(str_to_datetime(data_atual), dias)
                )
                write_json("data.json", data)
                print("Livro renovado com sucesso!")
                return True
    print("Livro não encontrado!")
    return False


def listar_emprestimos(data):
    for i in data["emprestimo"]:
        print(
            "Livro: {}, Cliente: {}, Data Emprestimo: {}, Prazo: {}, Devolvido: {}".format(
                i["livro"],
                i["cliente"],
                i["data_emprestimo"],
                i["prazo"] if i["devolvido"] == False else "Devolvido",
                i["devolvido"],
            )
        )


def menu_emprestimo():
    print("1 - Emprestar Livro")
    print("2 - Devolver Livro")
    print("3 - Listar Emprestimos")
    print("4 - Voltar")
    opcao = int(input("Digite a opção desejada: "))
    return opcao


if __name__ == "__main__":
    # emprestar_livro(get_json("data.json"), "l1", "c1", 5, devolvido=False)
    listar_emprestimos(get_json("data.json"))
    # emprestar_livro(get_json("data.json"), "l2", "c1", 5, devolvido=False)
    # renovar_emprestimo(get_json("data.json"), "c1", "l1", 5)
    # devolver_livro(get_json("data.json"), 'l1', 'c1')
