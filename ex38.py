a = int(input('Digite o primeiro número? '))
b = int(input('Digite o segundo número? '))
if a > b:
    print('O primeiro valor é maior'.format(a, b))
elif b > a:
    print('O segundo valor é maior'.format(b, a))
else:
    print('Não eixste valor maior, os dois são iguais'.format(a, b))