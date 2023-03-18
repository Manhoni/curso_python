r1=float(input('Primeiro segmento: '))
r2=float(input('Segundo segmento: '))
r3=float(input('Terceiro segmento: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os seguimentos escritos PODEM formar um triângulo!')
else:
    print('Os seguimentos escritos NÃO PODEM formar um triângulo.')
