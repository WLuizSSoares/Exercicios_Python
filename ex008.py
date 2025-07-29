valor = int(input("\033[7;35;41mDigite o valor em metros: "))
cent = valor*100
mili = valor*1000
print("\033[7;30mO vaLor em centimetros é {}cm, e milimetros é {}mm\033[m".format(cent, mili))