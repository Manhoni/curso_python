maior = 0
homens = 0
mm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mm20 += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if op == 'N':
        break
print(f'Temos um total de {maior} pessoas com mais de 18 anos.')
print(f'Tivemos {homens} homens cadastrados.')
print(f'E temos {mm20} mulheres com menos de 20 anos.')
