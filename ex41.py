from _datetime import date
nasc = int(input('Digite o ano do seu nascimento: '))
dataAtual = date.today().year
resultado = dataAtual - nasc
print(resultado)
if resultado <= 9:
    print('Mirin')
elif resultado > 9 and resultado <= 14:
    print('Infantil')
elif resultado > 14 and resultado <=19:
    print('Junior')
elif resultado == 20:
    print('Senior')
else:
    print('Master')