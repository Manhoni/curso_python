ano = int(2022)
times = ('Palmeiras',
        'Internacional',
        'Fluminense',
        'Corinthians',
        'Flamengo',
        'Athletico Paranaense',
        'Atlético Mineiro',
        'Fortaleza',
        'São Paulo',
        'América',
        'Botafogo',
        'Santos',
        'Goiás',
        'Red Bull Bragantino',
        'Coritiba',
        'Cuiabá',
        'Ceará',
        'Atlético',
        'Avaí',
        'Juventude')
print('-='*20)
print(f'BRASILEIRÃO {ano}')
print('-='*20)
print(f'Os 5 primeiros {times[0:5]}')
print(f'Os Rebaixados: {times[-4:]}')
print(f'Agora em ordem alfabetica para os com TOC: {sorted(times)}')
print(f'E o Grande Corinthians terminou na {times.index("Corinthians")+1}ª posição.')
