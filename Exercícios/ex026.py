#Faça um programa que leia uma frase pelo teclado:

frase = str(input('Digite uma frase: ')).upper().strip()
#Quantas vezes aparece a letra "A"
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))

#Em que posição ela aparece a primeira vez
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))

#Em que posição ela aparece a última vez
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))