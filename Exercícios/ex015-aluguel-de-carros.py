'''
Exercício Python 15: Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias pelos quais ele
foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por
dia e R$0,15 por Km rodado.
'''
dias = int(input('Quantos dias de locação?'))
km = float(input('Quantos KMs rodados?'))

tdias = dias*60
tkm = km*0.15

print('O carro foi alugado por {} dias e rodou {}km o custo total é R${:.2f}'.format(dias, km, float(tdias+tkm)))
