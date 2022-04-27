'''
Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''
nota1 = float(input('Nota1= '))
nota2 = float(input('Nota2= '))

media = (nota1 + nota2)/2

print ('Nota 1 foi {} \nNota 2 foi {} \nmédia foi {}'.format(nota1, nota2, media))