def fim():
    print('-=' * 18)
    print('         FIM DO PROGRAMA')
    print('-=' * 18)

def escreva(text):
    tamanho = len(text)
    print('=' * tamanho)
    print(text)
    print('=' * tamanho)


#main
texto = str(input('Digite um texto: ')).strip().capitalize()

escreva(texto)

fim()