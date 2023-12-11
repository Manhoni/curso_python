def leiaint(a):
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


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc
