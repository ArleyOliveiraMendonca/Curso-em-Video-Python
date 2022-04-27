# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# faça um program que ajude ele, lendo o nome dele e escrevendo o nome do escolhido

from random import choice

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))
