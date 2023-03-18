lista = []
c = 0
while True:
    c += 1
    lista.append(int(input('Digite um valor: ')))
    op = input('Deseja continuar? [S/N] ').strip().lower()
    if op in 'n':
        break
print(f'A) Foram digitados {c} números.') #sem contador é só usar o {len(lista)}
print(f'B) A lista ordenada de forma decrescente = {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'C) O valor 5 está na lista.')
else:
    print(f'C) O valor 5 não foi digitado portando não está na lista.')
