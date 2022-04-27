'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
no final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000,00
C) Qual é o nome do produto mais barato
'''

''' Esse é meu código...
compra = maismil = prod = 0

while True:
    produto = str(input('Nome do produto: '))

    preco = float(input('Preço do produto: '))
    menor = preco
    if menor < preco:
        print(f'{produto}')
    if preco > 1000:
        maismil += 1
    compra += preco
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'O total gasto foi R${compra:.2f}')
print(f'{maismil} custam mais de R$ 1000,00')
print(f'O produto mais barato custa R${menor} é o {produto}')
'''#fim do meu codigo
#Guanabara#
total = totmil = menor = cont = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40'.format(' Fim do Programa '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato custa R${menor:.2f}')
