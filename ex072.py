n = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
     'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
     'dezessete', 'dezoito', 'dezenove', 'vinte')
op = int(input('Digite um número entre 0 e 20: '))
while op < 0 or op > 20:
    op = int(input('Opção inválida, tente novamente: '))
print(f'Voçê digitou o número {n[op]}')
