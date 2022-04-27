'''
Faça um programa que leia um número qualquer e mostre o seu fatorial

ex:
5! = 5x4x3x2x1 = 120

from math import  factorial
'''

n = int(input('Qual o número para calcular o fatorial? '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c>1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
#print('O fatproaç de {} é {}'.format(n, f))


