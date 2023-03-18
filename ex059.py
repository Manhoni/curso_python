n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
lista = [n1, n2]
opção = 0
while opção != 5:
    print('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa')
    opção = int(input('Sua opção: '))
    if opção == 1:
        print(f'{n1}+{n2}={n1 + n2}.')
    if opção == 2:
        print(f'{n1}x{n2}={n1*n2}.')
    if opção == 3:
        print(f'O maior número é {max(lista)}')
    if opção == 4:
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
        lista = [n1, n2]
    if opção > 5:
        print('Opção inválida, tente novamente')
    print('-='*10)
print('Programa finalizado.')