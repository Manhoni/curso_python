termo = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for c in range(1, 11):
    if c == 1:
        print(f'a{c} = {termo}')
    else:
        termo += r
        print(f'a{c} = {termo}')
