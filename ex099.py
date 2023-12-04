from time import sleep

def fimprograma():
    print('-=' * 18)
    print('         FIM DO PROGRAMA')
    print('-=' * 18)

def maior(*num):
    tamanho = len(num)
    maiornum = max(num)
    print(f'\nAnalisando {tamanho} numeros...')
    sleep(1)
    print(f'O maior número inserido foi o {maiornum}.')


#main
maior(2, 3, 5)
maior(2,2,3,6,8,7,6, 9)

fimprograma()