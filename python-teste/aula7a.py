#nome = input('Qual é o seu nome?')
#print('Prazer em te conhecer {:=^20}!'.format(nome)) #a formatação determina que o nome vai ficar dentro de 20 espaços, centralizado e compleado com sinais de "="

n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma vale {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ') #":.3f" este codigo formata a impressão dos numeros flutuantes, "end=' '" este comando faz nao ter quebra de linha
print('Divisão inteira {} \n e potenciação {}'.format(di, e)) #"\n" este comando faz quebrar a linha
