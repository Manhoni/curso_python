flag = n = soma = 0
flag = int(input('Digite um número inteiro [Digite 999 para finalizar]: '))
while flag != 999:
    soma += flag
    n += 1
    flag = int(input('Digite um número inteiro [Digite 999 para finalizar]: '))
print(f'A soma dos números é {soma}')
print(f'Foram somados {n} números.')
