def fatorial(a, b='N'):
    f = 1
    for c in range(a, 0, -1):
        f *= c
    if b in 'S':
        return f
    else:
        print('FIM')


numero = int(input('Digite um valor inteiro para calcular seu fatorial: '))
opc = str(input('Agora digite se gostaria que fosse mostrado na tela [S/N]: ')).upper()

print(fatorial(numero, opc))
