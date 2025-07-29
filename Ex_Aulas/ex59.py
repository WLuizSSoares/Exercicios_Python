n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número: '))
opcao = 0
while opcao != 5:
    print(""" --Opções--
    [1] Somar
    [2] Multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa""")
    opcao = int(input('Qual sua escolha? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1*n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('Não há nenhum maior, os dois são iguais!!')
    elif opcao == 4:
        n1 = int(input('Qual o novo primeiro número? '))
        n2 = int(input('Qual o segundo primeiro número? '))
    else:
        print('Opção invalida')
print('Programa encerrado.')

