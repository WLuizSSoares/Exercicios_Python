from random import randint
print('=-'*25)
print('Vamos jogar par ou impar')
print('=-'*25)
computador = 0
quantidade = 0
while True:
    computador = randint(0, 11)
    numero = int(input('Diga um número: '))
    escolha = str(input('Par ou Ímpar? [P/I]')).lower().strip()[0]
    soma = computador + numero
    print(f'O computador escolheu {computador}, e você {numero}. Total de {soma} DEU PAR')

    if escolha == 'p':
        if soma %2 == 0:
            print('Você VENCEU!')
            quantidade +=1
        else:
            print('Você PERDEU!!')
            break
    if escolha == 'i':
        if soma %2 != 0:
            print('Você VENCEU!!')
            quantidade +=1
        else:
            print('Você PERDEU!!')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {quantidade} vezes')
print('fim')
