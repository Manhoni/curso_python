# existe modulo para fatorial (from math import factorial)
n = int(input('Escolha um número para saber seu fatorial: '))
n2 = 1
while n > 0:
    print(f'{n}', end='')
    print(f' x ' if n > 1 else ' = ', end='')
    n2 *= n
    n -= 1
print(n2)