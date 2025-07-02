def validador(cpf_digitado):

    organizar_cpf = []
    for char in cpf_digitado:
        try:
            organizar_cpf.append(int(char))
        except ValueError:
            continue

    if len(organizar_cpf) != 11:
        return False

    if organizar_cpf == [organizar_cpf[0]] * 11:
        return False

    soma1 = sum(organizar_cpf[i] * (10 - i) for i in range(9))
    dig1 = (soma1 * 10) % 11
    if dig1 == 10:
        dig1 = 0
    if organizar_cpf[9] != dig1:
        return False
    
    soma2 = sum(organizar_cpf[i] * (11 - i) for i in range(10))
    dig2 = (soma2 * 10) % 11
    if dig2 == 10:
        dig2 = 0
    if organizar_cpf[10] != dig2:
        return False

    return True
