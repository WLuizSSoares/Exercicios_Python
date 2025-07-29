km = float(input("Quantos km é sua viagem? "))
if km <= 200:
    passagem = 0.50*km
    print('O preço da sua passagem é de {}'.format(passagem))
else:
    passagem2 = 0.45*km
    print('o preço da sua passagem é de {}'.format(passagem2))
print('Tenha uma boa viagem!!')