termo = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
c = 0
while 0 <= c <= 9:
    print(f'{termo} + {r}', end='')
    termo += r
    c += 1
    print(f' = {termo}')
