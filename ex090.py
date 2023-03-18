faculdade = {}
faculdade['nome'] = str(input('Nome do aluno: '))
faculdade['media'] = float(input(f'Média de {faculdade["nome"]}: '))

if faculdade['media'] >= 6:
    faculdade['situacao'] = 'Aprovado'

else:
    faculdade['situacao'] = 'Reprovado'

for k, v in faculdade.items():
    print(f'{k} = {v}')
