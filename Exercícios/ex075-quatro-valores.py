'''
Desenvolva um programa que leia quatro valores plo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes aparece o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares.
'''

n1 = (int(input('Digite um número: ')), int(input('Digite mais um número: ')),int(input('Digite outro número: ')), int(input('Digite o último número: ')))

print(f'Você digitou os valores {n1}')
print(f'Quantas vezes o valor 9 pareceu: {n1.count(9)}')
if 3 in n1:
    print(f'o valor 3 apareceu na {n1.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhma posição')
print('Os valores pares digitados foram ', end='')
for n in n1:
    if n % 2 == 0:
        print(n , end=' ')
