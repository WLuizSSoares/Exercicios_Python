valores = []
pares = []
impares = []
for c in range (0, 8):
    num = int(input('Digite um número inteiro: '))
    if num in valores:
        print('Número repetido, não adicionado...')
    else:
        valores.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
print(f'Lista de pares: {pares}')
print(f'Lista de impares: {impares}')