from time import sleep
print('Comparador de números inteiros!')
print('-='*20)
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
print('Comparando...')
sleep(1)
if n1 > n2:
    print(f'O numero {n1} é maior que {n2}.')
elif n2 > n1:
    print(f'O número {n2} é maior que {n1}.')
else:
    print('Não existe valor maior, os dois são iguals.')
