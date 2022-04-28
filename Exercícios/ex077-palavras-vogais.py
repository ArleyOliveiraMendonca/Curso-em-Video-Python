'''
Crie um programa que tenha uma tupla com várias palavras (não use acentos).
Depois disso, você deve mostrar para cada palavra, quais sao as suas vogais.
'''

palavras = ('aprender', 'programar', 'linguagem', 'pyhon', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou': #lower faz as letras serem todas minusculas
            print(letra, end=' ')
