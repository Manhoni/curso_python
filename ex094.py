""" Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média """

pessoas = {}
lista = []
mulheres = []
maiormedia = []
soma_idade = 0

while True:
    pessoas['nome'] = str(input('\nDigite o nome da pessoa: ')).strip().capitalize()
    pessoas['sexo'] = str(input('Sexo: ')).capitalize()
    pessoas['idade'] = float(input('Idade: '))
    soma_idade += pessoas['idade']
    lista.append(pessoas.copy())

    while True:
        opt = str(input('\nDeseja inserir mais uma pessoa? [S/N]: ')).capitalize()

        if opt in ('N', 'S'):
            break
        else:
            print('Digite uma opção válida.')

    if opt in 'N':
        break

media = soma_idade / len(lista)

print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'A media de idade é {media:.2f} anos.')
print(f'Lista de mulheres:', end='')
for pessoas in lista:
    if pessoas.get('sexo') == 'F':
        print(f'{pessoas["nome"]}, ', end='')
print()

for pessoas in lista:
    if pessoas["idade"] > media:
        maiormedia.append(pessoas.copy())

print(f'Pessoa com idade acima da media que é {media} anos: \n{maiormedia}')




