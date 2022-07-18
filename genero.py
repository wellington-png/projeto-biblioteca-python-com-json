from utils import write_json, write_json, get_json, is_existe_genero


def cadastar_genero(data, nome):
    if is_existe_genero(data, nome):
        print('Genero ja cadastrado!')
        return data
    
    data['genero'].append({'id': len(data['genero']) + 1, 'nome': nome, "is_active": True})
    write_json('data.json', data)
    print('Gênero cadastrado com sucesso!')
    return data

def atualizar_genero(data, nome, novo_nome, is_active=True):
    for i in data['genero']:
        if i['nome'] == nome and i['is_active'] == True:
            i['nome'] = novo_nome
            i['is_active'] = is_active
            write_json('data.json', data)
            print('Operação realizada com com sucesso!')
            return data
    print('Gênero não encontrado!')
    return False

def apagar_genero(data,nome):
    atualizar_genero(data, nome, nome, False)
    return data

def listar_genero(data, is_active=True):
    for i in data['genero']:
        if i['is_active'] == is_active:
            print(i['id'], i['nome'])
    return data

def menu_genero():
    print('1 - Cadastrar Gênero')
    print('2 - Listar Gêneros')
    print('3 - Alterar Gênero')
    print('4 - Excluir Gênero')
    print('5 - Voltar')
    opcao = int(input('Digite a opção desejada: '))
    return opcao


if __name__ == '__main__':
    cadastar_genero(get_json('data.json'), 'filme')
