import os

from utils import (
    write_json,
    write_json,
    is_existe_genero,
    is_existe_autor,
    get_json,
    is_existe_livro,
)
from autor import cadastrar_autor
from genero import cadastar_genero


def cadastrar_livro(data, titulo, autor, genero, quantidade, disponivel, ano, codigo):
    j = autor
    i = genero
    autor = is_existe_autor(data, autor)
    genero = is_existe_genero(data, genero)

    if quantidade < 0:
        print("Quantidade não pode ser menor que zero!")
        return data
    if disponivel < 0:
        print("Disponivel não pode ser menor que zero!")
        return data
    if quantidade < disponivel:
        print("Quantidade não pode ser menor ou igual a disponivel!")
        return data

    if is_existe_livro(data, codigo):
        print("\nCodigo já cadastrado!\n")
        return data

    if not genero:
        t = cadastar_genero(data, i)
        genero = [True, t]

    if not autor:
        a = cadastrar_autor(data, j)
        autor = [True, a]

    data["livro"].append(
        {
            "id": len(data["livro"]) + 1,
            "titulo": titulo,
            "autor": autor[1],
            "genero": genero[1],
            "quantidade": quantidade,
            "disponivel": disponivel,
            "ano": ano,
            "codigo": str(codigo),
            "is_active": True,
        }
    )
    write_json("data.json", data)
    print("Livro cadastrado com sucesso!")
    return data


def atualizar_livro(
    data,
    codigo,
    titulo=None,
    autor=None,
    genero=None,
    quantidade=None,
    disponivel=None,
    ano=None,
    is_active=True,
):
    livro = is_existe_livro(data, codigo)
    if not livro:
        print("Livro não encontrado!")
        return data
    autor = is_existe_autor(data, autor)
    genero = is_existe_genero(data, genero)
    if not genero:
        print("Não foi possível atualizar o livro!, pois o genero ainda não existe!")
        return data
    if not autor:
        print("Não foi possível atualizar o livro!, pois o autor ainda não existe!")
        return data
    if quantidade < 0:
        print("Quantidade não pode ser menor que zero!")
        return data
    if disponivel < 0:
        print("Disponivel não pode ser menor que zero!")
        return data
    if quantidade < disponivel:
        print("Quantidade não pode ser menor ou igual a disponivel!")
        return data

    for i in data["livro"]:
        if i["id"] == livro[1] and i["is_active"] == True:
            i["titulo"] = titulo if titulo else i["titulo"]
            i["autor"] = autor[1] if autor else i["autor"]
            i["genero"] = genero[1] if genero else i["genero"]
            i["quantidade"] = quantidade if quantidade else i["quantidade"]
            i["disponivel"] = disponivel if disponivel else i["disponivel"]
            i["ano"] = ano if ano else i["ano"]
            i["codigo"] = codigo if codigo else i["codigo"]
            i["is_active"] = is_active if is_active else i["is_active"]
            write_json("data.json", data)  # atualiza o arquivo
            print("livro atualizado com sucesso!")
            return data


def apagar_livro(data, codigo):
    livro = is_existe_livro(data, codigo)
    if not livro:
        print("Livro não encontrado!")
        return data
    for i in data["livro"]:
        if i["id"] == livro[1] and i["is_active"] == True:
            i["is_active"] = False
            write_json("data.json", data)
            print("livro apagado com sucesso!")
            return data
    print("não encontrado!")
    return False


def listar_livro(data):
    print(
        f"{'ID':<5}{'TÍTULO':<35}{'AUTOR':<25}{'GÊNERO':<20}{'QUANTIDADE':<12}{'DISPONÍVEL':<12}{'ANO':<5}{'CÓDIGO':<8}"
    )
    print("-" * 145)
    for i in data["livro"]:
        if i["is_active"] == True:
            print(
                f' {i["id"]:<5}{i["titulo"]:<35}{data["autor"][i["autor"]-1]["nome_completo"]:<25}{data["genero"][i["genero"]-1]["nome"]:<20}{i["quantidade"]:<12}{i["disponivel"]:<12}{i["ano"]:<5}{i["codigo"]:<8}'
            )
            print("-" * 145)

    return data


def listar_livro_genero(data, genero):
    genero = is_existe_genero(data, genero)
    if not genero:
        print("Gênero não encontrado!")
        return False
    print(
        f"{'ID':<5}{'TÍTULO':<35}{'AUTOR':<25}{'GÊNERO':<20}{'QUANTIDADE':<12}{'DISPONÍVEL':<12}{'ANO':<5}{'CÓDIGO':<8}"
    )
    print("-" * 145)
    for i in data["livro"]:
        if i["is_active"] == True and i["genero"] == genero[1]:
            print(
                f' {i["id"]:<5}{i["titulo"]:<35}{data["autor"][i["autor"]-1]["nome_completo"]:<25}{data["genero"][i["genero"]-1]["nome"]:<20}{i["quantidade"]:<12}{i["disponivel"]:<12}{i["ano"]:<5}{i["codigo"]:<8}'
            )
            print("-" * 145)
    return data


def listar_livro_autor(data, autor):
    autor = is_existe_autor(data, autor)
    if not autor:
        print("Autor não encontrado!")
        return False
    print(
        f"{'ID':<5}{'TÍTULO':<35}{'AUTOR':<25}{'GÊNERO':<20}{'QUANTIDADE':<12}{'DISPONÍVEL':<12}{'ANO':<5}{'CÓDIGO':<8}"
    )
    print("-" * 145)
    for i in data["livro"]:
        if i["is_active"] == True and i["autor"] == autor[1]:
            print(
                f' {i["id"]:<5}{i["titulo"]:<35}{data["autor"][i["autor"]-1]["nome_completo"]:<25}{data["genero"][i["genero"]-1]["nome"]:<20}{i["quantidade"]:<12}{i["disponivel"]:<12}{i["ano"]:<5}{i["codigo"]:<8}'
            )
            print("-" * 145)
    return data


def livro_detalhes(data, codigo):
    livro = is_existe_livro(data, codigo)
    if not livro:
        print("Livro não encontrado!")
        return False
    print(
        f"{'ID':<5}{'TÍTULO':<35}{'AUTOR':<25}{'GÊNERO':<20}{'QUANTIDADE':<12}{'DISPONÍVEL':<12}{'ANO':<5}{'CÓDIGO':<8}"
    )
    print("-" * 145)
    for i in data["livro"]:
        if i["is_active"] == True and i["id"] == livro[1]:
            print(
                f' {i["id"]:<5}{i["titulo"]:<35}{data["autor"][i["autor"]-1]["nome_completo"]:<25}{data["genero"][i["genero"]-1]["nome"]:<20}{i["quantidade"]:<12}{i["disponivel"]:<12}{i["ano"]:<5}{i["codigo"]:<8}'
            )
            print("-" * 145)
    return data


def menu_livro(data):

    print("1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Listar Livros por Gênero")
    print("4 - Listar Livros por Autor")
    print("5 - Detalhar Livro")
    print("6 - Alterar Livro")
    print("7 - Excluir Livro")
    print("8 - Voltar")

    opcao = input("Digite a opção: ")
    if opcao.isdigit():
        opcao = int(opcao)

        if opcao == 1:

            print("Cadastrar Livro")
            titulo = input("Digite o titulo do livro: ")
            autor = input("Digite o nome do autor: ")
            genero = input("Digite o nome do gênero: ")
            codigo = input("Digite o código do livro: ")
            try:
                ano = int(input("Digite o ano do livro: "))
                quantidade = int(input("Digite a quantidade de livros: "))
                disponivel = int(input("Digite a quantidade de livros disponíveis: "))
            except ValueError:
                print("Erro! Digite apenas números!")
                menu_livro(data)

            cadastrar_livro(
                data, titulo, autor, genero, quantidade, disponivel, ano, codigo
            )

        elif opcao == 2:

            print("Listar Livros")
            listar_livro(data)

        elif opcao == 3:

            print("Listar Livros por Gênero")
            genero = input("Digite o nome do gênero: ")
            listar_livro_genero(data, genero)

        elif opcao == 4:

            print("Listar Livros por Autor")
            autor = input("Digite o nome do autor: ")
            listar_livro_autor(data, autor)
        elif opcao == 5:

            print("Detalhar Livro")
            codigo = input("Digite o código do livro: ")
            livro_detalhes(data, codigo)
        elif opcao == 6:

            print("Alterar Livro")
            codigo = input("Digite o código do livro: ")
            l = livro_detalhes(data, codigo)
            if l:
                titulo = input("Digite o titulo do livro: ")
                autor = input("Digite o nome do autor: ")
                genero = input("Digite o nome do gênero: ")
                ano = int(input("Digite o ano do livro: "))
                quantidade = input("Digite a quantidade de livros: ")
                disponivel = input("Digite a quantidade de livros disponíveis: ")

                if quantidade.isdigit():
                    quantidade = int(quantidade)
                else:
                    print("Quantidade de livros deve ser um número!")
                    menu_livro(data)
                if disponivel.isdigit():
                    disponivel = int(disponivel)
                else:
                    print("Quantidade de livros disponíveis deve ser um número!")
                    menu_livro(data)

                atualizar_livro(
                    data,
                    codigo,
                    titulo=titulo,
                    autor=autor,
                    genero=genero,
                    quantidade=quantidade,
                    disponivel=disponivel,
                    ano=ano,
                )
            else:
                menu_livro(data)
        elif opcao == 7:

            print(f"{' Excluir Livro ':=^80}")
            codigo = input("Digite o código do livro: ")
            livro_detalhes(data, codigo)
            opcao = input("Deseja excluir o livro? (S/N) ")
            if opcao.upper() == "S":
                apagar_livro(data, codigo)
        elif opcao == 8:
            return data
        else:
            print("Opção inválida!")
        menu_livro(get_json("data.json"))


if __name__ == "__main__":
    pass