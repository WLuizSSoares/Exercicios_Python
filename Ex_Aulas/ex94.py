relatorio = dict()
relatorio['nome'] = str(input("Nome do jogador: "))
partidas = int(input("Quantas partidas jogadas: "))
if partidas != 0:
    relatorio['gols'] = list()
    for c in range(1, partidas+1):
        numeroGols = int(input(f"Quantos gols na partida {c}? "))
        relatorio['gols'].append(numeroGols)
    relatorio['total'] = sum(relatorio['gols'])
    print('-=' * 30)
    print(relatorio)
    print('-=' * 30)
    for k, v in relatorio.items():
        print(f'O campo {k} tem o valor {v}.')
    print('-=' * 30)
    print(f"O jogador {relatorio['nome']} jogou {partidas} partidas.")
    for i, v in enumerate(relatorio['gols']):
        print(f'    => Na partida {i + 1}, fez {v} gols.')
    print(f"Foi um total de {relatorio['total']} gols.")
else:
    print('Não houve partidas, não há dados para calcular')