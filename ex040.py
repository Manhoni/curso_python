print('-='*20)
print('Calculo de média escolar!')
print('-='*20)
p1=float(input('Digite a nota da p1: '))
p2=float(input('Digite a nota da p2: '))
m = (p1+p2)/2
if m < 5:
    r = 'REPROVADO'
elif m >= 7:
    r = 'APROVADO'
else:
    r = 'DE RECUPERAÇÃO'
print(f'Sua média foi {m}, portanto vc está {r}.')
