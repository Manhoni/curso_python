print('Analizador de PALINDROMO!')
f = str(input('Digite uma frase: ')).strip().upper().split()
junto = ''.join(f)
inverso = ''
for l in range(len(junto)-1, -1, -1):
    inverso += junto[l]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo')
