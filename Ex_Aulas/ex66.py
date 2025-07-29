n = 0
soma = 0
quantidade = 0
while True :
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    quantidade += 1
print(f'Você digitou {quantidade} números e a soma entre eles é {soma}')