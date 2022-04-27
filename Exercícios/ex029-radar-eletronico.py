#Escreva um programa que leia a velocidade de um carro

#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado

#A multa vai custar R$ 7,00 a cada KM acima do limite

velocidade = float(input('Qual a velocidade o carro passou?: '))

if velocidade > 80:
    print('Você estava acima da velocidade permitida foi multado em R${:.2f}'.format((velocidade-80)*7))