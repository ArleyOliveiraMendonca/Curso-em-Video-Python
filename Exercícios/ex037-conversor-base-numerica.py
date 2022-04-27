#Escreva um programa que leia um número inteiro qualquer epeça pra o usuário escolher qual será a base de conversão:

# - 1 para binária
# - 2 para octal
# - 3 para hexadecimal

num = int(input('Digite um número ineiro: '))
print('''Escolha uma das bases pra conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido pra BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente')