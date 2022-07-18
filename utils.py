import json

def get_json(file_name):
    with open(file_name,) as f:
        data = json.load(f)
    return data

def write_json(file_name, data, encoding='utf-8'):
    with open(file_name, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def is_existe_genero(data, genero):
    for i in data['genero']:
        if i['nome'] == genero and i['is_active'] == True:
            return (True, i['id'])
    return False

def is_existe_autor(data, autor):
    for i in data['autor']:
        if i['nome_completo'] == autor and i['is_active'] == True:
            return (True, i['id'])
    return False

def is_existe_cliente(data, matricila):
    for i in data['cliente']:
        if i['matricula'] == matricila and i['is_active'] == True:
            return (True, i['id'])
    return False

def is_existe_livro(data, codigo):
    for i in data['livro']:
        if i['codigo'] == codigo and i['is_active'] == True:
            return (True, i['id'])
    return False

def estoque(data, livro):
    for i in data['livro']:
        if i['codigo'] == livro and i['disponivel'] > 0:
            print(i['disponivel'])
            return True
    return False

def pode_emprestar(data, matricula):
    for i in data['cliente']:
        if i['matricula'] == matricula and i['quant_possivel'] > 0:
            return True
    return False

def ja_emprestou(data, id):
    for i in data['emprestimo']:
        if i['cliente'] == id and i['devolvido'] == False:
            return False
    return True