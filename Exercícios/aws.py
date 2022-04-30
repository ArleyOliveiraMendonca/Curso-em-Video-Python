
for Number in range (1, 251):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')


    outfile = "results.txt"

    with open(outfile, "w") as file:
        file.write(str(Number))

    with open(outfile, "r") as arquivo:
        print(arquivo.read())
