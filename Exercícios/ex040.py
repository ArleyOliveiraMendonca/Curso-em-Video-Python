#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

nota1 = float(input('Prieira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1+nota2)/2

#Média abaixo de 5.0:
#Reprovado
if media < 5:
    print('Sua note foi {}, você foi REPROVADO'.format(media))
#Média entre 5.0 e 6.9
#Recuperação
#elif media >=5 and media <=6.9:
elif 7 > mmedia >=5:
    print('Sua nota foi {}, você esta de RECUPERAÇÃO'.format(media))

#Média 7.0 ou superior:
#Aprovado

else:
    print('Sua nota foi {}, parabéns você foi APROVADO!'.format(media))