print('-='*10)
print('Calculadora de IMC.')
print('-='*10)
alt = float(input('Digite a altura em METROS: '))
peso = float(input('Digite o peso em QUILOGRAMAS: '))
imc = peso / (alt**2)
print(f'seu IMC é de de {imc:.2f} ', end='')
if imc < 18.5:
    imc = 'ABAIXO DO PESO'
elif 18.5 <= imc < 25:
    imc = 'PESO IDEAL'
elif 25 <= imc < 30:
    imc = 'SOBREPESO'
elif 30 <= imc < 40:
    imc = 'OBESIDADE'
else:
    imc = 'OBESIDADE MÓRBIDA'
print(f'e está classificado como {imc}.')
