from random import randint
count = 0
npc = randint(0, 10)
n = int(input('Qual número eu pensei entre 0 e 10? : '))
while not npc == n:
    n = int(input('Você errou, tente novamente: '))
    count += 1
count += 1
print(f'Você acertou!! E com {count} tentativas.')
