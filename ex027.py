nome = str(input('Digite seu nome: ')).strip().title()
print(nome)
n = nome.split()
print(f'O primeiro nome é {n[0]} e o último é {n[len(n)-1]}')
