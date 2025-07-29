n = 0
soma = 0
quantidade = 0
while n != 999:
    n = int(input('Digite um número inteiro: '))
    if n !=999:
        soma += n
        quantidade +=1
if quantidade >1:
    print('Foram digitados {} números, e a soma entre eles é {}'.format(quantidade, soma))
elif quantidade <=1:
    print('Foi digitado apenas {} número, não há como somar:'.format(quantidade))
print('fim')