# Faça um programa que leia o ano de nascimeto de um jovem e informe, de acordo com sua idade:
#- Se ele ainda vai se alistar no serviço militar
#- Se está na época de se alistar
#- Se já passou do tempo de alistamento

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
nascimento = int(input('qual seu ano de nascimento: '))
hoje = date.today().year-nascimento

if hoje < 17:
    print('Voce tem {} anos, deve se alistar com 17 anos faltam {} para o alistamento!'.format(hoje,(17-hoje)))
elif hoje == 17:
    print('Você deve se alistar este ano')
else:
    print('Voce tem {} anos, deve ter se alistar com 17 anos já se alistou há {} anos!'.format(hoje,(hoje-17)))