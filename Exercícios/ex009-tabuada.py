'''
Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
'''
n = int(input('Qual o número? '))
print ('-' * 15)
print('| {} x  1 = {:>3} |'.format(n, n*1))
print('| {} x  2 = {:>3} |'.format(n, n*2))
print('| {} x  3 = {:>2} |'.format(n, n*3))
print('| {} x  4 = {:>2} |'.format(n, n*4))
print('| {} x  5 = {:>2} |'.format(n, n*5))
print('| {} x  6 = {:>2} |'.format(n, n*6))
print('| {} x  7 = {:>2} |'.format(n, n*7))
print('| {} x  8 = {:>2} |'.format(n, n*8))
print('| {} x  9 = {:>2} |'.format(n, n*9))
print('| {} x 10 = {:>2} |'.format(n, n*10))
print ('-' * 15)
