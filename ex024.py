cidade = str(input('Em qual cidade você nasceu? : ')).strip().capitalize()
#c = 'Santo'in cidade
#print(f'A cidade possui "Santo" no nome? {c}')
if 'Santo ' in cidade:
    print('A primeira palavra da sua cidade natal é Santo.')
else:
    print('A primeira palavra da sua cidade natal é diferente de Santo.')
