import random
from time import sleep
print('-' * 40)
num=int(input('Entre 0 e 5, qual número eu pensei? : '))
print('-' * 40)
numero=random.randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if num == numero:
    print('Aaa voce me venceu! PARABENS')
else:
    print(f'Não foi dessa vez, eu pensei no {numero}, você perdeu!')
