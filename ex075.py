n1 = (int(input('Número 1: ')),
    int(input('Número 2: ')),
    int(input('Número 3: ')),
    int(input('Número 4: ')))
print(f'Vc digitou os valores {n1}.')
print(f'A) O número 9 apareceu {n1.count(9)} vezes')
if 3 in n1:
    print(f'B) O número 3 apareceu primero na {n1.index(3) + 1}ª posição')
else:
    print('B) Não foi digitado número 3')
print(f'C) Os valores pares digitados foram: ', end='')
for n in n1:
    if n % 2 == 0:
        print(n, end=', ')
