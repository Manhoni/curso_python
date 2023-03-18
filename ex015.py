print('Calculo do valor a ser pago pelo contratante;')
d=int(input('Por quantos dias foi alugado? : '))
km=float(input('Quantos km foram rodados? :km '))
print(f'TOTAL: R${(d*60)+(km*0.15):.2f}.')
