from datetime import date

pessoa = {}

pessoa['nome']= str(input('Digite o nome: '))
nasc = int(input('Ano de nascimento: '))
anohoje = date.today().year
pessoa['idade'] = anohoje - nasc
pessoa['ctps']= int(input('Numero da carteira de trabalho(se não possuir digite 0): '))

if pessoa['ctps'] == 0:
    for k, v in pessoa.items():
        print(f'{k} : {v}')
else:
    pessoa['anocontrato']= int(input('Ano da contratação: '))
    pessoa['salario']= int(input('Salario: '))
    pessoa['aposentadoria']= pessoa['idade'] + ((pessoa['anocontrato'] + 35) - date.today().year)

    for k, v in pessoa.items():
        print(f'{k} : {v}')
