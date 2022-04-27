#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A média de idade
#O nome do homem mais velho
#Quantas mulheres tem menos de 21 anos

somaidade = 0
mediaidade = 0
maiordidadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiordidadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiordidadehomem:
        maiordidadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade/4
print('Amédia de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velhor tem {} anos e se chama {}.'.format(maiordidadehomem, nomevelho))
print('Ao todo são {} melheres com menos de 20 anos'.format(totmulher20))
