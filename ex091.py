from random import randint
from operator import itemgetter
jogadores = {}
jogo = []

for c in range(0, 4):
    jogadores['nome'] = str(input('Nome do jogador: '))
    jogadores['dado'] = randint(1, 6)
    jogo.append(jogadores.copy())

jogo = sorted(jogo, key=lambda k: (k['dado']), reverse=True)

for j in jogo:
    print(f'{jogo.index(j) + 1}º lugar: Jogador {j["nome"]} com {j["dado"]}.')
