from utilidadesCev import moeda
from ex108.formatacao import minhamoeda

p = float(input('Digite o preço: '))
print(f'A metade de {minhamoeda(p)} é {minhamoeda(moeda.metade(p))}')
print(f'Aumentando 10%, temos {minhamoeda(moeda.aumentar(p, 10))}')
print(f'O dobro de {minhamoeda(p, "US")} é {minhamoeda(moeda.dobro(p), "US")}')
print(f'Diminuindo 10% temos {minhamoeda(moeda.diminuir(p, 10))}')
