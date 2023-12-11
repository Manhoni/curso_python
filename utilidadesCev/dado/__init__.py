def leiadinheiro(dado):
    valido = False
    while not valido:
        entrada = str(input(dado)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido\033[m')
        else:
            valido = True
            return float(entrada)


def leiaint(a):
    """
      Integer checker, where take a value and return an integer.
      :param a: message that will apper for the user to enter the number.
      :return: returns an already validated integer value.
    """
    ok = False
    valor = 0
    while True:
        n = str(input(a))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mtype a numeric character.\033[m')
        if ok:
            break
    return valor
