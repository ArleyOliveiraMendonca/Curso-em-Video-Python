'''
Crie um programa que tenha uma tupla totalmente preenchida como uma contagem por extenso, de 0 a 20

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezessei', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um número entre [0 e 20] '))
    if 0 <= n <=20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {numero[n]}')

