galera = []
dados = []
max = min = 0
op = 'S'
while True:
    dados.append(str(input('Nome: ')).strip().upper())
    dados.append(int(input('Peso: ')))
    if len(galera) == 0:
        max = min = dados[1]
    else:
        if dados[1] > max:
            max = dados[1]
        if dados[1] < min:
            min = dados[1]
    galera.append(dados[:])
    dados.clear()
    op = input('Deseja inserir mais uma pessoa? [S/N]: ').upper()
    if op in 'N':
        break
print(f'Foram cadastradas {len(galera)} pessoas.')
print(f'O maior peso foi de {max}Kg. De ', end='')
for p in galera:
    if p[1] == max:
        print(f'{p[0]}')
print(f'O menor peso foi de {min}Kg. De ', end='')
for p in galera:
    if p[1] == min:
        print(f'{p[0]}')