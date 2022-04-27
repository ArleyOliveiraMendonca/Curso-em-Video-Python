#nome = str(input('Seu nome: '))

#if nome == 'Arley':
    #print('Que nome lindo você tem!')
#else:
    #print('Seu nome é normal.')
#print('Bom dia {}!'.format(nome))

#n1 = float(input('Digite a primeira nota: '))
#n2 = float(input('Digite a segunda nota: '))
#m = (n1+n2)/2

#print('A sua média foi {:.1f}'.format(m))
#if m>= 6.0:
#    print('Sua média foi muito boa! PARABÉNS!')
#else:
#    print("Sua média foi ruim! Estude mais")

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2

print('A sua média foi {:.1f}'.format(m))
print('Parabéns!' if m>=6.0 else 'Estude mais')