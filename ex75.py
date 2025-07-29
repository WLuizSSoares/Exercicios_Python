valores = []
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    valores.append(n)
tupla = tuple(valores)
print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 not in tupla:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O número 3 apareceu na {tupla.index(3) + 1} posição ')
pares = [num for num in tupla if num % 2 == 0]
print(f'Os valores pares digitados foram {pares}')