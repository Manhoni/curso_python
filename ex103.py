def ficha(a='desconhecido', b=0):
    if b == '':
        b = '<não informado>'
    if a == '':
        a = '<não informado>'
    print('Ficha jogador.')
    print(f'Nome do jogador: {a}')
    print(f'Gols marcados: {b}')


print('Criação da Ficha do Jogador.')
nome = str(input('Digite o nome: ')).strip().capitalize()
gols = input('Digite os gols marcados: ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = ''

ficha(nome, gols)
