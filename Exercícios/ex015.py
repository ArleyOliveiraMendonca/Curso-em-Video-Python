dias = int(input('Quantos dias de locação?'))
km = float(input('Quantos KMs rodados?'))

tdias = dias*60
tkm = km*0.15

print('O carro foi alugado por {} dias e rodou {}km o custo total é R${:.2f}'.format(dias, km, float(tdias+tkm)))
