#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

n1 = int(input('Qual o primeiro número: '))
n2 = int(input('Qual o segundo número: '))

if n1 > n2:
    print('O {} é maior que o {}'.format(n1, n2))
elif n2 > n1:
    print('O {} é maior que o {}'.format(n2, n1))
else:
    print('{} são iguais {}'.format(n1, n2))