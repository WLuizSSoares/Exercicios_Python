import time
import random
opcoes = ['Pedra', 'Papel','Tesoura']
print('\033[7;40m-+-\033[m'*10)
print('\033[7;40m Vamos começar a jogar jokenpô\033[m')
print('\033[7;40m-+-\033[m'*10)
comp = random.choice(opcoes).lower()
print(' ')
jogador = str(input('\033[1;31;40mEscolha entre:\033[m\n\033[1;34mPedra\nPapel\nTesoura\ne digite!\033[m\n ')).lower()
print(' ')
print('\033[7;40m Jo...\033[m')
time.sleep(1)
print('\033[7;40m Ken...\033[m')
time.sleep(1)
print('\033[7;40m Pô...\033[m')
time.sleep(1)
print(' ')
if jogador == comp:
    print('Empate')
elif jogador == 'papel':
    if comp == 'pedra':
        print('\033[1;33;36mVocê venceu!!\033[m')
    else:
        print('\033[1;31mVocê perdeu!!\033[m')
elif jogador == 'pedra':
    if comp == 'tesoura':
        print('\033[1;33;40mVocê venceu!!\033[m')
    else:
        print('\033[1;31mVocê perdeu!!\033[m')
elif jogador == 'tesoura':
    if comp == 'papel':
        print('\033[1;33;40mVocê venceu!!\033[m')
    else:
        print('\033[1;31mVocê perdeu!!\033[m')
else:
    print('Resposta inválida')
print(' ')
print('\033[1;37;40mO computador escolheu {}, e você {}\033[m'.format(comp, jogador))
