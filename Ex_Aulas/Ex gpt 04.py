valores = []
while True:
    mercado = str(input('Digite um item: ')).strip()
    if mercado.upper() != "SAIR":
        valores.append(mercado)
    else:
        print('Programa encerrado!')
        break
print(f'Sua lista: {valores}')