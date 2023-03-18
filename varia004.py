a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)} \n'
      f'Só tem espaços? {a.isspace()} \n'
      f'É alfabético? {a.isalpha()} \n'
      f'É alfanumérico? {a.isalnum()} \n'
      f'Está em maiúsculas? {a.isupper()} \n'
      f'Está em minúsculas? {a.islower()} \n'
      f'Está capitalizado? {a.istitle()}')
