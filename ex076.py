lista = ('pão', 1, 'leite', 3.50, 'cafe', 15, 'margarina', 5)
print('-'*40)
print('LISTA DE PREÇOS PADARIA'.center(40))
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<32}', end='')
    else:
        print(f'R${lista[pos]:>6.2f}')
print('-'*40)
