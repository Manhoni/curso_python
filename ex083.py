conta = input('Digite uma expressão matemática: ')
lista = [conta]
c9 = 0
c0 = 0
for c in conta:
    if c == '(':
        c9 += 1
    elif c == ')':
        c0 += 1
if c9 == c0:
    print('Essa expressão é válida.')
else:
    print('Essa expressão não é válida.')
