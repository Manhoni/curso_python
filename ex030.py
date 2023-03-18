n = int(input('Digite umk \033[36mnúmero\033[m qualquer: '))
print('-'*20)
if (n % 2) == 0:
    print(f'O número \033[32m{n}\033[m é \033[34mPAR\033[m')
else:
    print(f'O número \033[32m{n}\033[m é \033[31mIMPAR\033[m ')
