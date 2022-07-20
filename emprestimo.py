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
                    print("Livro emprestado com sucesso!\n")
                    return data["emprestimo"][-1]
                else:
                    print("Cliente com livro atrasado\n")
            else:
                print("Cliente ou Livro não possui quantidade disponível\n")
                return False
        else:
            print("Você já emprestou esse livro!\n")
            return False
    else:
        print("Livro ou cliente não encontrado!\n")
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
    print("Livro não encontrado!\n")
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
    print(f"\n{' Lista de emprestimos ':=^83}")
    print(f'{"Livro":<20}{"Socio":<20}{"Data Emprestimo":<17}{"Dias Devolução":<16}{"Prazo":<7}')
    print(f'{"-"*83}')
    for i in data["emprestimo"]:
        print(
            "{:<20}{:<20}{:^17}{:^17}{:<16}".format(
                data['livro'][i['livro'] - 1]['codigo'],
                data["cliente"][i['cliente'] - 1]["matricula"],
                i["data_emprestimo"],
                i["prazo"],
                'Devolvido' if i['devolvido'] else 'Pendente',
            )
        )
        print(f'{"-"*83}')
    
def listar_emprestimos_cliente(data, matricula):
    
    matricula = is_existe_cliente(data, matricula)
    if not matricula:
        print("Cliente não encontrado!")
        return False
        
    
    print(f"\n{' Lista de emprestimos ':=^83}")
    print(f'{"Livro":<20}{"Socio":<20}{"Data Emprestimo":<17}{"Dias Devolução":<16}{"Prazo":<7}')
    print(f'{"-"*83}')
    for i in data["emprestimo"]:
        
        if i['cliente'] == matricula[1]:
            print(
                "{:<20}{:<20}{:^17}{:^17}{:<16}".format(
                    data['livro'][i['livro'] - 1]['codigo'],
                    data["cliente"][i['cliente'] - 1]["matricula"],
                    i["data_emprestimo"],
                    i["prazo"],
                    'Devolvido' if i['devolvido'] else 'Pendente',
                )
            )
            print(f'{"-"*83}')
def listar_atrazados(data):
    print(f"\n{' Lista de emprestimos ':=^83}")
    print(f'{"Livro":<20}{"Socio":<20}{"Data Emprestimo":<17}{"Dias Devolução":<16}{"Prazo":<7}')
    print(f'{"-"*83}')
    for i in data["emprestimo"]:
        if i['devolvido'] == False:
            if i['prazo'] < data_atual:
                print(
                    "{:<20}{:<20}{:^17}{:^17}{:<16}".format(
                        data['livro'][i['livro'] - 1]['codigo'],
                        data["cliente"][i['cliente'] - 1]["matricula"],
                        i["data_emprestimo"],
                        i["prazo"],
                        'Devolvido' if i['devolvido'] else 'Pendente',
                    )
                )
                print(f'{"-"*83}')


def menu_emprestimo(data):
    print("1 - Emprestar Livro")
    print("2 - Devolver Livro")
    print("3 - Renovar Emprestimo")
    print("4 - Listar Emprestimos")
    print("5 - Listar Emprestimos Socio")
    print("6 - Listar Emprestimos Atrazados")
    print("7 - Voltar")
    
    try:
        opcao = int(input("Digite a opção: "))
    except:
        print("Opção inválida! \n")
        menu_emprestimo(data)
        
    if opcao == 1:
        cod_livro = input("Digite o código do livro: ")
        matricula = input("Digite a matricula do cliente: ")
        try:
            dias = int(input("Digite a quantidade de dias para devolução: "))
        except ValueError:
            print("Dias inválidos! \n")
            menu_emprestimo(get_json("data.json"))
        if dias <= 0:
            print("Dias inválidos! \n")
            menu_emprestimo(data)
        emprestar_livro(get_json("data.json"), cod_livro, matricula, dias)
        
    elif opcao == 2:
        cod_livro = input("Digite o código do livro: ")
        matricula = input("Digite a matricula do cliente: ")
        devolver_livro(get_json("data.json"), cod_livro, matricula)
    elif opcao == 3:
        matricula = input("Digite a matricula do cliente: ")
        cod_livro = input("Digite o código do livro: ")
        dias = int(input("Digite a quantidade de dias para devolução: "))
        renovar_emprestimo(get_json("data.json"), matricula, cod_livro, dias)
    elif opcao == 4:
        listar_emprestimos(get_json("data.json"))
    elif opcao == 5:
        matricula = input("Digite a matricula do cliente: ")
        listar_emprestimos_cliente(get_json("data.json"), matricula)
    elif opcao == 7:
        return True
    elif opcao == 6:
        listar_atrazados(get_json("data.json"))
    else:
        print("Opção inválida!")
        return False
    
    return menu_emprestimo(get_json("data.json"))


if __name__ == "__main__":
    pass