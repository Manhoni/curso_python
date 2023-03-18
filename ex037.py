print('-'*30)
print('Conversor numérico')
print('-'*30)
num = int(input('Digite o número a ser convertido: '))
var = int(input('[1] para binário\n[2] para octal\n[3] para hexadecimal\n'))
if var == 1:
    print(f'O numero {num} em binário é {bin(num)[2:]}.')
elif var == 2:
    print(f'O número {num} em octal é {num:o}.')
elif var == 3:
    print(f'O número {num} em hexadecimal é {num:x}.')
else:
    print('Opção de conversão digitada de forma incorreta, reinicie o programa.')
