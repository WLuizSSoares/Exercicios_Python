import random
gerador = tuple(random.sample(range(1, 11), 5 ))
print(f'Números sorteados {gerador}')
print(f'Maior valor: {max(gerador)}')
print(f'Menor valor: {min(gerador)}')
