'''
Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''
valor = float(input('Quanto dinheiro tem na carteira? '))
print ('Você tem R${:.2f} que corresponde a US${:.2f}'.format(valor, (valor/5.02)))
