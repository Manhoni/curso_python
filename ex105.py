'''
def notas():

    infos = {['nota'], ['situacao'], ['menor'], ['maior']}
    infos['total'] = len('nota')
    opc = ''
    maior = 0
    menor = 0
    media = 0
    situacao = ''
    soma = 0

    while True:
        notas = int(input("Digite a nota: "))
        infos.nota = notas
        soma += notas
        if notas < 6:
            infos.situacao = 'reprovado'
        elif notas > 6:
            infos.situacao = 'reprovado'
        opc = str(input("deseja inserir mais notas [S/N]: ")).upper()
        if opc == 'N':
            break

    for c in range(0, len(infos), +1):
        if c == 0:
            menor = infos.nota
            maior = infos.nota
        else:
            if infos.nota < menor:
                menor = infos.nota
            if infos.nota > maior:
                maior = infos.nota

    media = soma / infos['total']

    return infos

notas()
'''

def notas(*n, sit=False):
    """
    -> função para blablalbla
    :param n: uma ou varias notas
    :param sit: valor opcional indicando a sitação
    :return:dicionario com varias informações sobre notas.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 6:
            r['sitacao'] = 'aprovado'
        else:
            r['sitacao'] = 'reprovado'

    return r


#programa principal
resp = notas(9, 5.5, 2.5, 8.5, sit=True)
print(resp)
print('')
help(notas)