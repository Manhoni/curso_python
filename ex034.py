sal=float(input('Digite o salário do funcionário: R$ '))
print('$'*20)
if sal <= 1250:
    print(f'O salário atualizado para 2023 é R${sal*(15/100)+sal:.2f} com aumento de 15%.')
else:
    print(f'O salária atualizado em 10% para 2023 é R${sal*(10/100)+sal:.2f}.')
print('$'*20)
