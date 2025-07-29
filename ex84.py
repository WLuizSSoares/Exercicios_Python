pessoas = list()
dados = list()
mai = men = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite o seu peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    cond = input('Deseja continuar [S/N]: ').strip().upper()
    pessoas.append((dados[:]))
    dados.clear()
    if cond != 'S':
        break
print('-='*30)
print(f'Os dados foram {pessoas}')
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {mai}kg. Peso de', end='')
for p in pessoas:
    if p[1] == mai:
        print(f' {p[0]}', end='')
print('')
print(f'O menor peso foi de {men}kg. Peso de', end='')
for p in pessoas:
    if p[1] == men:
        print(f' {p[0]}', end='')
