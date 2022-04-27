'''
Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
de tinta pinta uma área de 2 metros quadrados.
'''
l = float(input('Qual a largura? '))
h = float(input('Qual a altura? '))

m = l*h

print('Altura é {} a largura é {} essa parede tem {}m², necessita de {}l para pintá-la'.format(l, h, m, m/2))
