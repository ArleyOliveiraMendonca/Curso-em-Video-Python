'''
Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''
n = int(input('Qual o número?'))

print('O número escolhido foi {} \nseu dobro é {} \nseu triplo é {} \ne sua raiz qudrada é {:.4f}'.format(n, n*2, n*3, n**(1/2)))