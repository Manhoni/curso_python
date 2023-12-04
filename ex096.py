def area(a, b):
    if a == b:
        formato = 'quadrado'
    else:
        formato = 'retângulo'
    area = a * b
    print(f'\nA area do {formato} é {area} m².')

def fim():
    print('-=' * 20)
    print('         FIM DO PROGRAMA')
    print('-=' * 20)


#main
comprimento = float(input('COMPRIMENTO(m): '))
largura = float(input('LARGURA(m): '))

area(comprimento, largura)

fim()