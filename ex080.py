lista = []
for c in range(0, 5):
    if c == 0:
        lista.append(int(input('Digite um valor: ')))
        print('Adicionado ao final da lista')
    else:
        n = int(input('Digite um valor: '))
        if n > max(lista):
            lista.append(n)
            print('Adicionado ao final da lista')
        elif n < min(lista):
            lista.insert(0, n)
            print('Adicionado na posição 0 da lista')
        else:
            lista.insert(1, n)
            print('Adicionado na posição 1 da lista')
print(lista)
