#Desenvolva um programa que leia seis números ineiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
soma = 0
cont = 0
for c in range(1, 7):
    n1 = int(input('Digite o {} vlor: '.format(c)))
    if n1 % 2 == 0:
        soma += n1
        cont +=1
print('Voce informou {} números e a soma foi {}'.format(cont, soma))