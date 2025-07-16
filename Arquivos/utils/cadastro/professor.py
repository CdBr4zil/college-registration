import os

from utils.gerar_id_ra import gerar_id
from utils.confirmacao import confirmar_dado
from utils.cadastro.cursos import listar_cursos

professores_cadastrados = []

def cad_prof():
    
    lista_cursos = listar_cursos()
    if not lista_cursos:
        print("Nenhum curso cadastrado ainda!\n")
        return

    print("--Cadastro de Professor--\n")

    nome = confirmar_dado("Digite o nome do Professor: ")
    nascimento = confirmar_dado(f"Digite a data de nascimento de {nome} (dd-mm-aaaa): ")
    cpf = confirmar_dado(f"Digite o CPF de {nome}: ", tipo='cpf')
    endereco = confirmar_dado(f"Digite o endereço de {nome}: ")
    
    print("Cursos disponíveis:\n")
    for indice, nome_curso in enumerate(lista_cursos):
        print(f"{indice+1} - {nome_curso}")
    print()

    while True:
        try:
            escolha = int(input("Selecione o número do curso: ")) - 1
            if 0 <= escolha < len(lista_cursos):
                curso_nome = lista_cursos[escolha]
                break
            else:
                print("\nOpção inválida. Tente novamente.\n")
        except ValueError:
            print("\nDigite apenas números válidos.\n") #Precisa ver um jeito de dar cls e retornar a lista dps

    identificacao = gerar_id()

    professor = {
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco,
        "curso": curso_nome,
        "identificacao": identificacao
    }
    professores_cadastrados.append(professor)

    os.system('cls')
    print("Professor cadastrado com sucesso!\n")
    print("-" * 40)
    print(f"Nome           : {nome}")
    print(f"Nascimento     : {nascimento}")
    print(f"CPF            : {cpf}")
    print(f"Endereço       : {endereco}")
    print(f"Curso          : {curso_nome}")
    print(f"Identificação  : {identificacao}")
    print("-" * 40)

def listar_professores():
    return [prof["nome"] for prof in professores_cadastrados]
