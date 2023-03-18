from random import randint
from time import sleep
c = 0
while True:
    op = str(input('Par ou Ímpar? : ')).strip().upper()
    n = int(input('Digite seu número: '))
    pc = randint(1, 5)
    print('Computador joga...')
    sleep(1.5)
    print(f'...{pc}!')
    if op == 'PAR':
        if (n + pc) % 2 == 0:
            c += 1
            print('PARABÉNS, vc venceu!')
        if (n + pc) % 2 == 1:
            print('Que tistreza, vc perdeu...')
            break
    if op == 'IMPAR':
        if (n + pc) % 2 == 1:
            c +=1
            print('PARABENS, vc ganhou!')
        if (n + pc) % 2 == 0:
            print('Que tistreza, vc perdeu...')
            break
    print('Vamos jogar novamente!')
    print('-='*12)
print('-='*20)
print(f'Você conseguiu {c} vitória(s)!')
