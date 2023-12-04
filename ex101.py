import datetime

def voto(a):
    if a < 16:
        return 'NEGADO'
    elif 17 < a < 60:
        return 'OBRIGATÓRIO'
    else:
        return 'OPICIONAL'


print('CONSULTA SITUAÇÃO ELEITORAL.')
ano = int(input('Digite o ano de nascimento: '))
idade = datetime.datetime.now().year - ano
print(F'{idade} anos: VOTO {voto(idade)}')
