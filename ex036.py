print('-='*20)
print('Análise de empréstimo imobiliário')
print('-='*20)
nome = str(input('Bom dia! Poderia por favor nos dizer o seu nome? ')).strip().title()
casa = float(input(f'Obrigado {nome}, agora nos diga o valor da casa a ser comprada: '))
sal = float(input('Salário do comprador: R$ '))
ano = int(input('Em quantos anos pretende pagar: '))
paga = (30/100)*sal
parcela = casa / (ano*12)
print(f'A parcela desejada ficaria em R${parcela:.2f}.')
if parcela > paga:
    print('O emprestimo foi \033[31mNEGADO\033[m!')
else:
    print('O empréstimo foi \033[32mAPROVADO\033[m!')
print('-'*30)
print(f'Muito obrigado pela confiança em nossos serviços {nome}')
print('Encerrando a consulta.')
