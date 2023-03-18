from datetime import date
hj = date.today().year
p = 0
m = 0
print('MOSTRADOR DE MAIORIDADE CONSIDERANDO MAIORIDADE COM 21 ANOS')
print('-='*20)
for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = hj - ano
    if idade >= 21:
        print('Maior de idade.')
        p += 1
    else:
        print('Menor de idade.')
        m +=1
print('-='*20)
print(f'{p} pessoas desta lista são maior de idade.')
print(f'{m} pessoas desta lista são menor de idade.')
