from datetime import date
hoje = date.today().year
nasc = int(input('Digite o ano de nascimento do atleta: '))
dif = hoje - nasc
if dif <= 9:
    cat = 'mirim'
elif dif > 9 and dif <= 14:
    cat = 'infantil'
elif 19 >= dif > 14:
    cat = 'junior'
elif dif > 19 and dif <= 20:
    cat = 'sênior'
else:
    cat = 'master'
print(f'A idade do atleta é {dif} e ele se enquadra na categoria {cat}.')
