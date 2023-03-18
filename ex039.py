from datetime import datetime
nome = str(input('Por favor digite seu nome: ')).strip().title()
genero = str(input('Você se considera homem ou mulher? : ')).strip().capitalize()
ano = int(input('Digite o ano do seu nascimento: '))
now = datetime.now()
idade = now.year - ano
dif = idade - 18
if genero == 'Mulher':
    print(f'{nome} você não precisa se alistar no Brasil.')
else:
    if dif >= 1:
        print(f'Ja passou do tempo de se alistar em {dif} anos.')
    elif dif == 0:
        print('Este é o ano de se alistar!')
    elif dif <= -1:
        print(f'Deve se alistar em {dif} anos.')
    elif genero == 'Mulher':
        print(f'{nome}, você não precisa se alistar no Brasil.')
