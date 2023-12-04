from time import sleep

def fimprograma():
    print('-=' * 18)
    print('         FIM DO PROGRAMA')
    print('-=' * 18)

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print(f'\nContagem de {i} ate {f} de {p} em {p}.')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont+= p
        print('...FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('...FIM')


#main
contador(1, 10, 1)
contador(10, 0, 2)
print('\nPersonalize a contagem')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

fimprograma()