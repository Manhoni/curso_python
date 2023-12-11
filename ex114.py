import urllib
import urllib.request


def testesite():
    try:
        site = urllib.request.urlopen('http://www.pudim.com.br')
    except:
        print('O site não está acessivel')
    else:
        print('Site disponível')


testesite()
