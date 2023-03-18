sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()
    if sexo == 'M':
        print('A pessoa é homem.')
    elif sexo == 'F':
        print('A pessoa é mulher.')
    else:
        print('Voce digitou errado, digite M para masculino e F para feminino.')
