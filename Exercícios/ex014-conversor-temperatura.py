'''
Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''
temp = float(input('Qual a temperatura?'))

print('A temperatura em Celsius é {} \ne em Fahrenheit é {} \n e em Kelvin'.format(temp,((temp*9/5)+32)), (temp+273.15))
