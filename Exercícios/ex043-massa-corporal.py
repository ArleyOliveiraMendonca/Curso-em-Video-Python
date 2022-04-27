# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#
# - Abaixo de 18.5: Abaixo do peso
#
# - Entre 18.5 e 25: Peso ideal
#
# - Entre 25 e 30: Sobrepeso
#
# - Entre 30 e 40: Obesidade
#
# - Acima de 40: Obesidade mórbida

altura = float(input('Qual sua altura: '))
peso = float(input('Qual seu peso: '))

imc = peso/altura**2

if imc <= 18.5:
    print('{:.2f} Abaixo do peso'.format(imc))
elif imc <= 25:
    print('{:.2f} Peso ideal'.format(imc))
elif imc <= 30:
    print('{:.2f} Sobrepeso'.format(imc))
elif imc <= 40:
    print('{:.2f} Obesidade'.format(imc))
else:
    print('{:.2f} Obesidade Mórbida'.format(imc))
