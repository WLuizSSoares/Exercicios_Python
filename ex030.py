n = int(input('Digite um número inteiro: '))
par = n % 2
if par == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é impar'.format(n))