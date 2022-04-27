#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
#Ex: Ana Maria de Souza
#primeiro=Ana
#último=Souza

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito praer em te conhecer, seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
