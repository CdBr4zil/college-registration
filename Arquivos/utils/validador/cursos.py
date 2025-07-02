def confirmar_dado(pergunta):
    while True:
        valor = input(pergunta).strip().upper()
        confirmar = input(f"Confirma '{valor}'? (S/N): ").strip().upper()
        if confirmar == 'S':
            return valor
        elif confirmar == 'N':
            print("Digite novamente...\n")
        else:
            print('Caracter incorreto')
            return confirmar


def curso():
    
    print("Cadastro de Curso\n")

    nome = confirmar_dado("Digite o nome do Curso: ")
    professor = confirmar_dado(f"Selecione o professor do curso: ")

    print("\nCadastro finalizado com sucesso!")
    print(f"Nome: {nome}")

aluno()