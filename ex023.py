n=int(input('Digite um número entre 0 e 9999: '))
u=n//1%10
d=n//10%10
c=n//100%10
m=n//1000%10
print(f'A unidade de {n} é {u};')
print(f'A dezena de {n} é {d};')
print(f'A centena de {n} é {c};')
print(f'E o milhar de {n} é {m}.')
