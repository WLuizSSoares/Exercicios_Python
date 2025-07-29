while True:
    n = int(input('Quer saber a tabuada de qual número? '))
    if n < 0:
        print('Programa encerrado.')
        break
    print(f'Tabuada do número {n}')
    print('-' * 20)
    for c in range(1, 11):
        mult = c*n
        print(f'{n} x {c} = {mult}')
    print('-' * 20)