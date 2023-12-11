def leiaint(a):
    """
      Integer checker, where take a value and return an integer.
      :param a: message that will apper for the user to enter the number.
      :return: returns an already validated integer value.
    """
    while True:
        try:
            n = int(input(a))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero inteiro.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[031mUsuário preferiu não digitar o valor.\033[m')
            return '/'
        else:
            return n


def leiafloat(a):
    while True:
        try:
            n = float(input(a))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero real.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[031mUsuário preferiu não digitar o valor.\033[m')
            return '/'
        else:
            return n


i = leiaint('Digite um numero inteiro: ')
f = leiafloat('Digite um numero real: ')
print(f'Voce digitou o numero inteiro {i} e o real foi {f:.2f}.')
