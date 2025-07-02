from .validador.validador_cpf import validador
import os

def confirmar_dado(pergunta, tipo=None):
    while True:
        valor = input(pergunta).strip().upper()

        if tipo == 'cpf':
            if not validador(valor):
                os.system('cls')
                print("⚠️ CPF inválido. Digite novamente.\n")
                continue

        confirmar = input(f"Confirma '{valor}'? (S/N): ").strip().upper()
        if confirmar == 'S':
            os.system('cls')
            return valor
        elif confirmar == 'N':
            os.system('cls')
            print("Digite novamente...\n")
            break
        else:
            os.system('cls')
            print("⚠️ Caracter inválido. Digite apenas 'S' ou 'N'.\n")

