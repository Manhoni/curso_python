while True:
    print('')
    n = int(input('Quer saber a tabuada de qual número? : '))
    if n < 0:
        break
    c = 0
    for l in range(1, 11):
        c += 1
        print(f'{n} x {c} = {n*c}')
print('-=' * 18)
print('Obrigado por usar nosso programa!')
