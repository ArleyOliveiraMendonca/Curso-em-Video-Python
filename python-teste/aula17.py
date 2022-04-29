a = [2, 3, 4, 7, ]
b = a[:] # Assim se faz uma copia de cada item do "a" dando autonomia ao "b"
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
