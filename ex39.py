from _datetime import date
nasc = int(input('Em que ano você nasceu?  '))
dataAtual = date.today().year
resultado = dataAtual - nasc
print(resultado)
prePrazo = 18 - resultado
posPrazo = abs(24 - resultado)
if resultado < 18:
    print('Você ainda vai se alistar ao serviço militar')
    print('Ainda faltam {} ano(s) para o seu alistamento'.format(prePrazo))
elif resultado >= 18 and resultado <= 24:
    print("Está na hora de se alistar ao serviço militar")
else:
    print('Já passou da hora de se alistar ao serviço militar')
    print('Você passou {} ano(s) do prazo de alistamento'.format(posPrazo))