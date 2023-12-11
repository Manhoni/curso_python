from utilidadesCev import moeda
from ex108 import formatacao

p = float(input('Digite o preço: '))
print(f'A metade de {formatacao.minhamoeda(p)} é {moeda.metade(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'O dobro de {formatacao.minhamoeda(p, "US")} é {formatacao.minhamoeda(moeda.dobro(p), "US")}')
print(f'Diminuindo 10% temos {formatacao.minhamoeda(moeda.diminuir(p, 10))}')
