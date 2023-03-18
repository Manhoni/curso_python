from unidecode import unidecode
frase = str(input('Digite uma frase qualquer: ')).strip().lower()
frase = unidecode(frase)
print(f'A letra "a" aparece {frase.count("a")} vezes.')
print(f'A primeira vez ela aparece na posição {frase.find("a")+1}')
print(f'A última vez que ela aparece é na posição {frase.rfind("a")+1}')
