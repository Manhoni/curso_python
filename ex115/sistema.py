from ex115.lib.interface import *
from ex115.lib.arquivotxt import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoa', 'Sair do Sistema'])
    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        cadastrar(arq)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(1.5)
