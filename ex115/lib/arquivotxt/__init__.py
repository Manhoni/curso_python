from ex115.lib.interface import *
from time import sleep


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
        #existis cursoemvideo.txt in pasta:
        #create txt in local
        #print(f'Arquivo {txt} criado com sucesso.')
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a.close()


def cadastrar(nome):
    try:
        a = open(nome, 'at')
    except:
        print('Erro ao cadastrar.')
    else:
        while True:
            pessoa = str(input('Digite o nome: ')).strip()
            capitalizado = ' '.join(palavra.capitalize() for palavra in pessoa.split())
            idade = leiaint('Digite a idade: ')
            a.write(f'{capitalizado:<30} \t{idade:>3} anos\n')
            opc = ''
            #opc = str(input('Deseja inserir mais uma pessoa? [S/N]: ')).upper()
            while True:
                opc = str(input('Deseja inserir mais uma pessoa? [S/N]: ')).upper()
                if opc in ('N', 'S'):
                    break
                else:
                    print('Digite S para sim ou N para não: ')
            if opc == 'N':
                break
        a.close()
        cabecalho('CADASTRANDO...')


