from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print(f'{" JOKENPO ":=^20}')
#esc = str(input('Escolha entre PEDRA, PAPEL ou TESOURA: ')).strip().upper()
print('Digite sua opção\n[0] PEDRA\n[1]PAPEL\n[2]TESOURA')
esc = int(input('Qual sua escolha: '))
pc = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
print('-='*14)
print(f'Computador jogou {itens[pc]}.')
print(f'Jogador jogou {itens[esc]}.')
print('-='*14)
if pc == 0: #pc jogou pedra
    if esc == 0:
        print('EMPATOU!')
    elif esc == 1:
        print('JOGADOR GANHOU!')
    elif esc == 2:
        print('COMPUTADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 1: #pc jogou papel
    if esc == 0:
        print('COMPUTADOR GANHOU!')
    elif esc == 1:
        print('EMPATOU!')
    elif esc == 2:
        print('JOGADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 2: #pc jogou tesoura
    if esc == 0:
        print('JOGADOR GANHOU!')
    elif esc == 1:
        print('COMPUTADOR GANHOU!')
    elif esc == 2:
        print('EMPATOU!')
    else:
        print('JOGADA INVÁLIDA!')
