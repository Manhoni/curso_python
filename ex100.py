import random
from time import sleep

def fimprograma():
    print('-=' * 18)
    print('         FIM DO PROGRAMA')
    print('-=' * 18)

def sorteia():
    i = 0
    print('\nSorteando 5 numeros inteiros: ', end='')
    for i in range (0, 5):
        numero = random.randint(1, 10)
        numeros.append(numero)
        i += 1
        sleep(0.5)
        print(f'{numero}', end=', ')
    #print(f'\nOs numeros sorteados foram {numeros}.')

def somapar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'\nA soma dos pares é {soma}.')


#main
numeros = []

sorteia()
sleep(1)
print('')
somapar()
sleep(1)
fimprograma()