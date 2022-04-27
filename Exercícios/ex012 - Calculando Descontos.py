'''
Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''
p = float(input('Qual o preço? '))

print('Este produto custa R${:.2f} com o desconto fica por R${:.2f}'.format(p, p*0.95))
