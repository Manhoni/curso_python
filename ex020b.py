from random import shuffle
lista = str(input('Digite o nome dos quatro alunos separados por vírgula: ')).split(',')
shuffle(lista)
print(f'A sequência para apresentação dos trabalhos da turma é:\n {lista}')
