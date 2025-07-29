import random
numeroRandom = random.randint(0, 10)
nUsuario = int(input('Qual número eu pensei de 0 a 10? '))
tentativas = 0
while nUsuario != numeroRandom:
    nUsuario = int(input('Errado, chute mais uma vez: '))
    tentativas += 1
print('Você acertou, e precisou de {} tentativas'.format(tentativas))
