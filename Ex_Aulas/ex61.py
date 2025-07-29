n = int(input('Digite um número inteiro: '))
a = 0
b = 1
contador = 2
print('{} -> {}'.format(a, b), end='')
while contador < n:
    proximo = a + b
    print(' -> {}'.format(proximo), end='')
    a = b
    b = proximo
    contador += 1
print(' -> FIM')