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


#main
n = leiaint('Digite um numero: ')
print(f'Voce digitou o numero {n}.')
