import os

from utils.confirmacao import confirmar_dado

cursos_cadastrados = [] #Lista temporaria

def cad_curso():
    print("--Cadastro de Curso--\n")

    nome_curso = confirmar_dado("Digite o nome do Curso: ")
    cursos_cadastrados.append(nome_curso)
    
    os.system('cls')
    print("\nCadastro finalizado com sucesso!")
    print("-" * 40)
    print(f"Curso cadastrado: {nome_curso}")
    print("-" * 40 + "\n")

def listar_cursos():
    return cursos_cadastrados
