n = int(input('Digite um número para fatorar: '))
fatorial = 1
contador = n
while contador > 0:
    print(contador, end=" ")
    print('x ' if contador > 1 else '= ', end ='')
    fatorial *= contador
    contador -=1
print(fatorial)