from time import sleep
'''lista = []
listapar = []
listaimpar = []
for n in range(0, 7):
    num = (int(input(f'Número {n+1}: ')))
    if num % 2 == 0:
        listapar.append(num)
        lista.append(listapar[:])
    else:
        listaimpar.append(num)
        lista.append(listaimpar[:])
    listapar.clear()
    listaimpar.clear()
sorted(lista)
print(f'Os números digitados em ordem crescente são:{lista}.')'''

lista = [[], []]
num = 0
for n in range(0, 7):
    num = int(input(f'Número {n+1}: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print('-='*20)
lista[0].sort()
lista[1].sort()
print('Ordenando os números em ordem crescente...')
sleep(1.5)
print(f'Os valores pares digitados foram : {lista[0]}.')
print(f'Os valores ímpares digitados foram: {lista[1]}.')
