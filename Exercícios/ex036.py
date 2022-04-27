#Escreva um programa para aprovar o emprestimo bancário pra a compra de uma casa. O programa vai perguntar o valor da casa,
#o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento: '))

parcela =  anos*12
valor_parcela = valor / parcela

salario_disponível = (salario)*30/100

if valor_parcela <= salario_disponível:
    print('Salário: R${:.2f} \n Valor da casa: R${:.2f} \n Parcelas é {} \n Limite de investimento: R${:.2f} \n Valor da parcela: R${:.2f} \n Parabéns seu imprestimo APROVADO'.format(salario, valor, parcela, salario_disponível,valor_parcela))
else:
    print('Salário: R${:.2f} \n Valor da casa: R${:.2f} \n Parcelas é {} \n Limite de investimento: R${:.2f} \n Valor da parcela: R${:.2f} \n INFELIZMENTE seu imprestimo NEGADO'.format(salario, valor, parcela, salario_disponível,valor_parcela))

