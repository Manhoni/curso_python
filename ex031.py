km = int(input('Quanto Km voce percorreu nesta viagem? : '))
if km <= 200:
    print(f'O valor da passagem ficou \033[32mR${km*0.5:.2f}\033[m.')
else:
    print(f'O valor da passagem ficou \033[32mR${km*0.45:.2f}\033[m')
#if km <= 200:
#   preço = km *0.5
#else:
#   preço = km *0.45
#print(f'O valor da sua passagem será R${preço}.')
