palavras = ('banana', 'abacate', 'suco', 'refri', 'pizza', 'salsicha', 'bolo', 'pudim')
for v in palavras:
    print(f'\nEm {v.upper()} temos as vogais ', end='')
    for letra in v:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')