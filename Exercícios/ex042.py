#Refaça o desafio 035 dos triaângulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
#
# - Equilátero: Todos os lados iguais
#
# - Isóceles: dois lados iguais
#
# - escaleno: todos os lados diferentes
#
#
print('-=' * 20)
print('Analizndo Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if r1 == r2 == r3:
        print('Equilatero')

    elif (r1 == r2 and r1 != r3) or (r1 == r3 and r1 != r2) or (r3 == r2 and r3 != r1):
        print('Isoceles')
    else:
        print('Escaleno')

else:
    print('Os segmentos NÃO PODEM formar triângulo')

