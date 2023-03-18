lista = []
for n in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um valor para [{n}, {c}]: '))
        lista.append(num)
print('-=' * 17)
cont = 0
for n in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[cont]:^5}]', end='')
        cont +=1
    print()
