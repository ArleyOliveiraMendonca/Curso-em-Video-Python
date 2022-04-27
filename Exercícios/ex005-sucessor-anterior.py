'''
Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
'''
valor = int(input('Qual o valor? '))
print('O valor escolhido foi {} seu antecessor é {} seu socessor é {}'.format(valor, (valor-1), (valor+1)))

