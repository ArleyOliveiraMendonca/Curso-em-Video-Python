

from random import randint
from  time import sleep
computador = randint(0,5) #sorteio

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)
if computador == jogador:
    print('Parabéns, o número que pensei foi {} e você acertou!'.format(computador))
else:
    print('Você ainda não acertou, pensei no número {} e você colocou o {} ?'.format(computador, jogador))