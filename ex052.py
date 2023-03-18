p = 0
num = int(input('Digite um número inteiro: '))
for c in range(1, num+1):
    if num % c == 0:
        p += 1
if p == 2:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} NÃO é primo.')
