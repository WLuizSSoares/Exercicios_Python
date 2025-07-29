import random
numeroRandom = random.randint(0, 5)
#print(numeroRandom)
nUsuario = int(input('Qual número eu pensei de 0 a 5? '))
if numeroRandom == nUsuario:
    print('O número é {} e você acertou, PARABÉNS!!'.format(numeroRandom))
else:
    print('Que pena, tente novamente, o número correto era {}'.format(numeroRandom))