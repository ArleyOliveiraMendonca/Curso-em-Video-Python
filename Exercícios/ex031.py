#Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200km
#e R$ 0,45 para viagens mais longas

distancia = float(input('Qual a distância?'))

if distancia <= 200:
    print('Sua viagem vai custar R$ {:.2f}'.format(distancia*0.5))
else:
    print('Sua viagem vai custar R$ {:.2f}'.format(distancia*0.45))
