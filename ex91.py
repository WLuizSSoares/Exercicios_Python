import time
from random import randint
jogador = dict()
jogo = list()
tempo_de_pausa = 1.5
print('-=' *30)
print('Rolando o dado...')
print('-=' *30)
time.sleep(tempo_de_pausa)
for i in range(1, 5):
    jogador["nome"] = f'Jogador{i}'
    jogador["numero"] = randint(1, 6)
    print(f'{jogador["nome"]} jogou o dado e tirou: {jogador["numero"]}')
    time.sleep(tempo_de_pausa)
    jogo.append(jogador.copy())
print('Ranking de jogadores: ')
ranking = sorted(jogo, key=lambda item: item["numero"], reverse=True)
for i, j in enumerate(ranking):
    print(f' {i +1}° lugar: {j["nome"]} com {j["numero"]}')