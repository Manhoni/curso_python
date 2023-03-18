from random import randint
from time import sleep
jogo = []
todos = []
cont = 0
jogos = int(input('Digite o número de jogos: '))
#print('-=' * 16)
print(f"{'SORTEADOR DA MEGA SENA':-^32}")
#import random
#for x in range(int(input('Number of games: '))):
#    print(f'Game {x+1}: {random.sample(range(1, 60), 6)}')

for c in range(0, jogos):
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break

    cont = 0
    jogo.sort()
    sleep(1)
    print(f'Jogo {c + 1} = {jogo}')
    todos.append(jogo)
    jogo.clear()

print('-=' * 16)
print('BOA SORTE!'.center(32))
