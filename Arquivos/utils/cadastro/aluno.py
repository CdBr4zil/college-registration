import os

from utils.gerar_id_ra import gerar_ra
from utils.confirmacao import confirmar_dado
from utils.cadastro.cursos import listar_cursos

alunos_cadastrados = []

def cad_aluno():

    lista_cursos = listar_cursos()
    if not lista_cursos:
        print("Nenhum curso cadastrado ainda!\nPor favor cadastre um curso primeiro!")
        return
    
    print("--Cadastro de Aluno--\n")

    nome = confirmar_dado("Digite o nome do Aluno: ")
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
            os.system('cls')
            print("\nDigite apenas números válidos.\n")

    registro_academico = gerar_ra()

    aluno = {
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco,
        "curso": curso_nome,
        "registro_academico": registro_academico
    }
    alunos_cadastrados.append(aluno)

    os.system('cls')
    print("Aluno cadastrado com sucesso!\n")
    print("-" * 40)
    print(f"Nome              : {nome}")
    print(f"Nascimento        : {nascimento}")
    print(f"CPF               : {cpf}")
    print(f"Endereço          : {endereco}")
    print(f"Curso             : {curso_nome}")
    print(f"Registro Acadêmico: {registro_academico}")
    print("-" * 40 + "\n")

def listar_alunos():
    return [aluno["nome"] for aluno in alunos_cadastrados]
