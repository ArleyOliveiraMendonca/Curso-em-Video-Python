#Faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Qual o peso? '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi {}kg'.format(menor))
