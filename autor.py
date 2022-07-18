from utils import write_json, write_json, is_existe_autor, get_json


def cadastrar_autor(data, nome_completo):
    if is_existe_autor(data, nome_completo):
        print('Autor ja cadastrado!')
        return data
    data['autor'].append({'id': len(data['autor']) + 1, 'nome_completo': nome_completo, "is_active": True})
    write_json('data.json', data)
    print('Autor cadastrado com sucesso!')
    return data

def atualizar_autor(data, nome, novo_nome, is_active=True):
    for i in data['autor']:
        if i['nome_completo'] == nome and i['is_active'] == True:
            i['nome_completo'] = novo_nome
            i['is_active'] = is_active
            write_json('data.json', data)
            print('autor atualizado com sucesso!')
            return data
    print('não encontrado!')
    return False

def apagar_autor(data,nome):
    atualizar_autor(data, nome, nome, False)
    return data

def listar_autor(data, is_active=True):
    for i in data['autor']:
        if i['is_active'] == is_active:
            print(i['id'], i['nome_completo'])
    return data

def menu_autor():
    print('1 - Cadastrar Autor')
    print('2 - Listar Autores')
    print('3 - Alterar Autor')
    print('4 - Excluir Autor')
    print('5 - Voltar')
    opcao = int(input('Digite a opção desejada: '))
    return opcao

if __name__ == '__main__':
    cadastrar_autor(get_json('data.json'), 'José')
