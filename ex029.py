velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80.0:
    print('Você foi multado, o limite de velocidade é 80km/h!!!')
    multa = (velocidade-80)*7
    print("O valor da multa é {:.2f}".format(multa))
print('Tenha um bom dia, dirija com cuidado!!')
