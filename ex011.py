valor1 = float(input('Qual é a altura da parede: '))
valor2 = float(input('Qual é a largura da parede: '))
area = valor1*valor2
tinta = area/2
print("A área da parede é {:.2f}m², e são necessário {:.2f}l de tinta".format(area, tinta))
