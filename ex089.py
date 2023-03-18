ficha = []
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('P1: '))
    nota2 = float(input('P2: '))
    media = (nota2 + nota1) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp in 'N':
        break
print('-=' * 13)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    print('-' * 26)
    opc = int(input('Deseja mostrar as notas de qual aluno? (999 para interromper o programa): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print(f'{"Programa finalizado":^26}')
