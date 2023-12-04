jogador = {}
totalgols = []

jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
jogos = jogador['partidas']

for c in range(0, jogos):
    gols = int(input(f'Quantos gols marcou na partida {c + 1}: '))
    totalgols.append(gols)

jogador['gols feitos'] = totalgols

print('-=' * 13)
print(jogador)

print('-=' * 13)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')

print('-=' * 13)

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i, v in enumerate (jogador['gols feitos']):
    print(f'    => Na partida {i + 1}, fez {v}.')
print(f'Foi um total de {jogador["gols feitos"]} gols')