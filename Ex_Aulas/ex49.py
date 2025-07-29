n = int(input('Digite um valor para você saber a tabuada: '))
print("Tabuada")
for c in range(0, 11):
    mult = c * n
    print("{} * {} = {}".format(n, c, mult))