lista1 = []
listapar = []
listaimpar = []
while True:
    lista1.append(int(input('Digite um valor: ')))
    op = input('Deseja continuar? [S/N] ').strip().lower()
    if op in 'n':
        break
for c in lista1:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)
print('-='*18)
print(f'A lista completa é {lista1}.')
print(f'A lista de pares é {listapar}.')
print(f'A lista dos ímpares é {listaimpar}.')
