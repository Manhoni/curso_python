lista = []
listapar = []
coluna3 = []
linha2 = []
for n in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um valor para [{n}, {c}]: '))
        lista.append(num)
        if num % 2 == 0:
            listapar.append(num)
        if c == 2:
            coluna3.append(num)
        if n == 1:
            linha2.append(num)
print('-=' * 17)
cont = 0
for n in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[cont]:^5}]', end='')
        cont +=1
    print()

print('-='*17)
print(f'A soma dos valores pares é {sum(listapar)}.')
print(f'A soma dos valores da terceira coluna é {sum(coluna3)}.')
print(f'O maior valor da segunda linha é {max(linha2)}.')
