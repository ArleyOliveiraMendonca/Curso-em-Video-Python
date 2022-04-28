'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de numeros gerados e também indique o menor e o aior valor que estão na tupla.
'''

from random import randint
n = (randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)),
print(f'Os valores sorteados foram: ', end='')
for n in n:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
