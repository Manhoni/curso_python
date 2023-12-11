from ex108.formatacao import moeda


def aumentar(n=0, porc=0, formato=False):
    res = n + (n * (porc/100))
    return res if formato is False else moeda(res)


def diminuir(n=0, porc=0, formato=False):
    res = n - (n * (porc/100))
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if not formato else moeda(res)


def metade(n=0, formato=False):
    res = n / 2
    return res if not formato else moeda(res)


def resumo(preco=0, taxaa=15, taxar=10):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)
