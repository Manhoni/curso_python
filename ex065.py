flag = 'S'
lista = []
cont = soma = 0
num = int(input('Digite um valor inteiro: '))
while flag == 'S':
    soma += num
    lista.append(num)
    flag = str(input('Deseja continuar inserindo valores? [S/N] : ')).strip().upper()
    cont += 1
    if flag == 'S':
        num = int(input('Digite um valor inteiro: '))
    if flag == 'N':
        print('Inserção finalizada.')
print('-='*20)
print(f'O maior valor digitado é {max(lista)} e o menor é {min(lista)}.')
m = soma / cont
print(f'E a média dos valores digitados é {m:.2f}.')
