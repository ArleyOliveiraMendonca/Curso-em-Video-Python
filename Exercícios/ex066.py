'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual doi oa soma entre eles
(desconsiderando o flag)
'''
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')