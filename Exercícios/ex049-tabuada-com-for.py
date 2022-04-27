#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, so que agora utilizando um laço for

t = int(input('Qual a tabuada? '))

for i in range(0, 11):
    print('{} x {} = {}'.format(t,i, (t*i)))
print('Fim')