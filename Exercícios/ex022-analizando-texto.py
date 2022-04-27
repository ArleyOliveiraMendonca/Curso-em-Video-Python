# Crie um programa que leia o nome completo de uma pessoa e mostre?
#nome = str(input('Nome: '))
#sobrenome = str(input('Sobrenome: '))

nome = str(input('Digite seu nome completo: ')).strip()

#print('{} {}'.format(nome, sobrenome))

print('Analisando seu nome: {}'.format(nome))

# O nome com todas as letras maiúsculas
print('seu nome em maiúsculas é {}'.format(nome.upper()))

# O nome com todas as minúsculas
print('Seu nome em minúsculas é {}'.format(nome.lower()))

# Qual o total de letras (sem considerar os espaços)
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))

# Quantas letras tem o primeiro nome
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))



