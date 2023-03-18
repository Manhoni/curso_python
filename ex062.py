from time import sleep
print('-='*20)
print('GERADOR DE P.A.')
print('-='*20)
termo = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
c = 0
total = 0
op = 10
while op != 0:
    total += op
    while c <= total:
        print(f'{termo} + {r}', end='')
        termo += r
        c += 1
        print(f' = {termo}')
    op = int(input('Quantos termos deseja mostrar a mais? Digite 0 para parar : '))
print('Finalizando...')
sleep(1.5)
print(f'Programa finalizado mostrando {total} termos.')
