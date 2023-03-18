num = int(input('Escolha o número que deseja saber a tabuada: '))
for c in range(1, 11):
    tab = num * c
    print(f'{num} x {c} = {tab}')
