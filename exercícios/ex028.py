import random
from time import sleep
c = random.randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
j = int(input('Em que número eu pensei? '))
sleep(2)
if j == c:
    print('parabéns! Você conseguiu me vencer!')
else:
    print(f'ganhei! Eu pensei no número {c} e não no {j}!')
