from registro_ra import gerar_ra
from confirmacao import confirmar_dado

def cad_prof():
    print("Cadastro de Professor\n")

    nome = confirmar_dado("Digite o nome do Professor: ")
    nascimento = confirmar_dado(f"Digite a data de nascimento de {nome} (dd-mm-aaaa): ")
    cpf = confirmar_dado(f"Digite o CPF de {nome}: ", tipo='cpf')
    endereco = confirmar_dado(f"Digite o endereço de {nome}: ")
    curso = confirmar_dado(f"Digite o curso de {nome}: ")
    registro_academico = gerar_ra()

    print("Cadastro finalizado com sucesso!\n")
    print(f"Nome: {nome}")
    print(f"Data de nascimento: {nascimento}")
    print(f"CPF: {cpf}")
    print(f"Endereço: {endereco}")
    print(f"Curso: {curso}")
    print(f"Registro Acadêmico: {registro_academico}")

cad_prof()