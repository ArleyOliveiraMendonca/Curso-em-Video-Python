'''
Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''
valor = int(input('Qual o valor '))
print('O valor em metros é {}m \nem centimetros é{}cm \ne em milimetros é {}mm'.format(valor, valor*100, valor*1000))
