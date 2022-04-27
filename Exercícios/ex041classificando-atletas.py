#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
#e mostre sua categora, de acordo com a idade:
#
#-Até 9 anos: Mirim
#-Até 14 anos: Infantil
#-Ate 19 anos: Junior
#-até 20 anos: Sênior
#-Acima: Master

from datetime import date

nascimento = int(input('Qual seu ano de nascimento?'))
idade = date.today().year-nascimento

if idade <= 9:
    print('Este(a) atleta tem {} anos, se enquadra no nível MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Este(a) atleta tem {} anos, se enquadra no nível INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Este(a) atleta tem {} anos se enquadra no nível JUNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('Este(a) atleta tem {} anos se enquadra no nível SÊNIOR'.format(idade))
else:
    print('Este(a) atleta tem {} anos se enquadra no nível MASTER'.format(idade))