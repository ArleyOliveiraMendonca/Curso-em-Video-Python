#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
#Para salários superiores a R$ 1250,00, calculet um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual o salário? '))

if salario <= 1250:
    print('Seu salário é de R$ {:.2f} com o aumento de R$ {:.2f} passará a ser R$ {:.2f}'.format(salario, (salario*1.15)-salario, salario*1.15))
else:
    print('Seu salário é de R$ {:.2f} com o aumento de R$ {:.2f} passará a ser R$ {:.2f}'.format(salario, (salario*1.10)-salario, salario*1.10))
