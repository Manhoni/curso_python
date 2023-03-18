numeros = []
for num in range(0, 5):
    numeros.append(int(input('Digite um valor: ')))
print(f'O maior valor encontrado é o {max(numeros)}, na posição ', end='')
for c, v in enumerate(numeros):
    if v == max(numeros):
        print(f'{c}...', end='')
print(f'\nE o menor valor é o {min(numeros)}, na posição ', end='')
for c, v in enumerate(numeros):
    if v == min(numeros):
        print(f'{c}...', end='')
