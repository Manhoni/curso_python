s = 0
count = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c} número inteiro: '))
    if num%2==0:
        s += num
        count += 1
print(f'Soma de {count} números pares é {s}')
