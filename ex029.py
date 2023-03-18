from time import sleep
vel=int(input('Informe a velocidade em K/m detectada pelo radar: '))
multa = vel - 80
print('Checando limites...')
sleep(2)
print('-'*30)
if vel > 80:
    print(f'O veículo foi \033[31mmultado\033[m\n'
          f'O valor da multa é \033[32mR${multa*7:.2f}\033[m\n'
          f'Passe no Detran da sua cidade para regularizar.')
else:print('Velocidade \033[36mdentro\033[m do limite.')
print('-'*30)
