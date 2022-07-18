from utils import write_json, write_json, is_existe_genero, is_existe_autor, get_json, is_existe_livro


def cadastrar_livro(data, titulo, autor, genero, quantidade, disponivel, ano, codigo):
    autor = is_existe_autor(data, autor)
    genero = is_existe_genero(data, genero)
    if not genero:
        print('Não foi possível cadastrar o livro!, pois o genero ainda não existe!')
        return data
    if not autor:
        print('Não foi possível cadastrar o livro!, pois o autor ainda não existe!')
        return data
    
    print(autor)
    if quantidade < 0:
        print('Quantidade não pode ser menor que zero!')
        return data
    if disponivel < 0:
        print('Disponivel não pode ser menor que zero!')
        return data
    if quantidade <= disponivel:
        print('Quantidade não pode ser menor ou igual a disponivel!')
        return data
    
    if is_existe_livro(data, codigo):
        print('Livro ja cadastrado!')
        return data

    data['livro'].append({'id': len(data['livro']) + 1, 'titulo': titulo, 'autor': autor[1], 'genero': genero[1], 'quantidade': quantidade, 'disponivel': disponivel, 'ano': ano, 'codigo': codigo, "is_active": True})
    write_json('data.json', data)
    print('Livro cadastrado com sucesso!')
    return data

def atualizar_livro(data, codigo, titulo=None, autor=None, genero=None, quantidade=None, disponivel=None, ano=None, is_active=True):
    livro = is_existe_livro(data, codigo)
    print(livro)
    if not livro:
        print('Livro não encontrado!')
        return data
    autor = is_existe_autor(data, autor)
    genero = is_existe_genero(data, genero)
    if not genero:
        print('Gênero não encontrado!')
        return data
    if not autor:
        print('Autor não encontrado!')
        return data
    if quantidade < 0:
        print('Quantidade não pode ser menor que zero!')
        return data
    if disponivel < 0:
        print('Disponivel não pode ser menor que zero!')
        return data
    if quantidade < disponivel:
        print('Quantidade não pode ser menor ou igual a disponivel!')
        return data

    for i in data['livro']:
        if i['id'] == livro[1] and i['is_active'] == True:
            i['titulo'] = titulo if titulo else i['titulo']
            i['autor'] = autor[1] if autor else i['autor']
            i['genero'] = genero[1] if genero else i['genero']
            i['quantidade'] = quantidade if quantidade else i['quantidade']
            i['disponivel'] = disponivel if disponivel else i['disponivel']
            i['ano'] = ano if ano else i['ano']
            i['codigo'] = codigo if codigo else i['codigo']
            i['is_active'] = is_active if is_active else i['is_active']
            write_json('data.json', data) # atualiza o arquivo
            print('livro atualizado com sucesso!')
            return data

def apagar_livro(data, codigo):
    livro = is_existe_livro(data, codigo)
    if not livro:
        print('Livro não encontrado!')
        return data
    for i in data['livro']:
        if i['id'] == livro[1] and i['is_active'] == True:
            i['is_active'] = False
            write_json('data.json', data)
            print('livro apagado com sucesso!')
            return data
    print('não encontrado!')
    return False

def listar_livro(data):
    for i in data['livro']:
        if i['is_active'] == True:
            print(i['id'], i['titulo'], i['autor'], i['genero'], i['quantidade'], i['disponivel'], i['ano'], i['codigo'])
    return data

def listar_livro_genero(data, genero):
    genero = is_existe_genero(data, genero)
    if not genero:
        return data
    for i in data['livro']:
        if i['is_active'] == True and i['genero'] == genero[1]:
            print(i['id'], i['titulo'], i['autor'], i['genero'], i['quantidade'], i['disponivel'], i['ano'], i['codigo'])
    return data

def listar_livro_autor(data, autor):
    autor = is_existe_autor(data, autor)
    if not autor:
        return data
    for i in data['livro']:
        if i['is_active'] == True and i['autor'] == autor[1]:
            print(i['id'], i['titulo'], i['autor'], i['genero'], i['quantidade'], i['disponivel'], i['ano'], i['codigo'])
    return data

def menu_livro():
    print('1 - Cadastrar Livro')
    print('2 - Listar Livros')
    print('3 - Alterar Livro')
    print('4 - Excluir Livro')
    print('5 - Voltar')
    opcao = int(input('Digite a opção desejada: '))
    return opcao
    

if __name__ == '__main__':
    # cadastrar_livro(get_json('data.json'), 'senhor', 'José', 'filme', 10, 5, 2000, '12983')
    # atualizar_livro(get_json('data.json'), '129y83', 'titulo', 'João', 'filme', 5, 2, 2000, is_active=True)
    # apagar_livro(get_json('data.json'), '12983')
    # listar_livro(get_json('data.json'))
    listar_livro_genero(get_json('data.json'), 'filme')
    listar_livro_autor(get_json('data.json'), 'José')