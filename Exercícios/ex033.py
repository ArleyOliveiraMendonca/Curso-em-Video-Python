#Faça um programa que leia três números e mostre qual é maior e qual é menor

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#Verificando qual o menor
menor = a
if b<a and b<c:
    menor =b
if c<a and c<b:
    menor = c

#Verificando qual o maior
maior = b
if a>b and a>c:
    maior = a
if c>a and c>b:
    maior = c

print('o Maior número é {} e o menor número é {}'.format(maior, menor))