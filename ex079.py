lista = []
while True:
    n = int(input('Digite um valor: '))
    # lista.append(int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar.')
    op = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if op in 'n':
        break
print(f'Os valor digitados em ordem crescente são {sorted(lista)}')
