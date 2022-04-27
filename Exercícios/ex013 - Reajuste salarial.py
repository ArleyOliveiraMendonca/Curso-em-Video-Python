'''
Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''
s = float(input('Qual o salário atual?'))

print('O salário atual é R${:.2f} o novo salário será R${:.2f}'.format(s, s*1.15))
