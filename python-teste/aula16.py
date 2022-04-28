lanche = ('Hamburguer', 'Suco', 'Pizza', 'pudim', 'batata-frita')

print(sorted(lanche)) #organiza em ordem alfabetica
print(lanche)
'''
print(lanche)
print(lanche[1])# referencia com colchetes - mostra suco
print(lanche[-2])# le ao contrario, mostra a Pizza
print(lanche[3]) # mostra pudim
print(lanche[1:3])# mostra elemento 1 e 2 suco e pizza por que desconsidera o ultimo
print(lanche[2:])#do 2 ao final
print(lanche[:2])# do inicio ao elemento 2 desconsiderando o ultimo
print(lanche[-2:])# coeça na pizza e vai ate o final
print(lanche[-3:])# vai mostrar do suco ate o final
print(len(lanche))#mostra a lista da tupla
print('-='*10)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('-='*10)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('-='*10)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('-='*10)'''


