'''
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''
valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
valores.sort()
pares.sort()
impares.sort()
print('-=' * 30)
print(f'A lista completa é{valores}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {impares}')
print('-=' * 30)

