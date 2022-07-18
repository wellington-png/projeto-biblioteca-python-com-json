from cliente import cadastar_cliente
from utils import write_json, write_json, get_json, is_existe_genero, is_existe_livro, is_existe_cliente, pode_emprestar, ja_emprestou, estoque

def emprestar_livro(data, livro, cliente, data_emprestimo, data_devolucao, devolvido=False):
    livro_id = is_existe_livro(data, livro)
    cliente_id = is_existe_cliente(data, cliente)
    if livro_id and cliente_id:
        if ja_emprestou(data, cliente_id[1]):
            if pode_emprestar(data, cliente) and estoque(data, livro):
                # if data_emprestimo > data_devolucao:
                #     print('Data de emprestimo maior que data de devolução!')
                #     return data
                data['emprestimo'].append({'id': len(data['emprestimo']) + 1, 'livro': livro_id[1], 'cliente': cliente_id[1], 'data_emprestimo': data_emprestimo, 'data_devolucao': data_devolucao, 'devolvido': devolvido})
                t = livro_id[1] - 1
                c = cliente_id[1] - 1
                data['livro'][t]['disponivel'] -= 1
                data['cliente'][c]['quant_possivel'] -= 1
                write_json('data.json', data)
                return data['emprestimo'][-1]
            else:
                print('Cliente não pode emprestar!')
                return False
        else:
            print('Cliente ja emprestou!')
            return False
    else:
        print('Livro ou cliente não encontrado!')
        return False

def menu_emprestimo():
    print('1 - Emprestar Livro')
    print('2 - Devolver Livro')
    print('3 - Listar Emprestimos')
    print('4 - Voltar')
    opcao = int(input('Digite a opção desejada: '))
    return opcao
    

if __name__ == '__main__':
    emprestar_livro(get_json('data.json'), '1111', '123', '2020-01-01', '2020-01-31')
    