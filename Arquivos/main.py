import os

from utils.cadastro.professor import cad_prof, listar_professores
from utils.cadastro.aluno import cad_aluno, listar_alunos
from utils.cadastro.cursos import cad_curso, listar_cursos

if __name__ == "__main__":

    while True:

        menu_principal = input('--Selecione uma opção--\n[C]adastro [V]er listas [S]air: ').upper()

        if menu_principal == 'C':
            os.system('cls')
            while True:
                menu_cadastro = input('--Selecione uma opção de cadastro--\n[A]luno [P]rofessor [C]urso [S]air: ').upper()
                if menu_cadastro == 'A':
                    os.system('cls')
                    cad_aluno()
                elif menu_cadastro == 'P':
                    os.system('cls')
                    cad_prof()
                elif menu_cadastro == 'C':
                    os.system('cls')
                    cad_curso()
                elif menu_cadastro == 'S':
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                    print('Essa opção não existe!\n')

        elif menu_principal == 'V':
    
            os.system('cls')
            while True:
                menu_ver = input('--Ver listas--\n[A]lunos [P]rofessores [C]ursos [S]air: ').upper()
                if menu_ver == 'A':
                    lista_alunos = listar_alunos()
                    if not lista_alunos:
                        os.system('cls')
                        print("Nenhum curso cadastrado ainda!\nPor favor cadastre um curso primeiro!\n")
                        break
                    os.system('cls')
                    listar_alunos()
                elif menu_ver == 'P':
                    lista_profs = listar_professores()
                    if not lista_profs:
                        os.system('cls')
                        print("Nenhum curso cadastrado ainda!\nPor favor cadastre um curso primeiro!\n")
                        break
                    os.system('cls')
                    listar_professores()
                elif menu_ver == 'C':
                    lista_cursos = listar_cursos()
                    if not lista_cursos:
                        os.system('cls')
                        print("Nenhum curso cadastrado ainda!\nPor favor cadastre um curso primeiro!\n")
                        break
                    os.system('cls')
                    listar_cursos
                elif menu_ver == 'S':
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                    print('Essa opção não existe!\n')

            
        elif menu_principal == 'S':
                os.system('cls')
                break

        else:
            os.system('cls')
            print('Essa opção não existe!\n')
