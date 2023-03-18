somaidade = 0
maisvelho = 0
velho = ''
mulher20 = 0
for c in range(1, 5):
    print(f'-----{c}ª pessoa-----')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().upper()
    somaidade += idade
    if c == 1 and sexo == 'M':
        maisvelho = idade
        velho = nome
    if sexo == 'M' and idade > maisvelho:
        maisvelho = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        mulher20 += 1
mediagrupo = somaidade / 4
print(f'A média de idade do grupo é {mediagrupo} anos.')
print(f'{velho} é o homem mais velho e tem {maisvelho} anos.')
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos.')
