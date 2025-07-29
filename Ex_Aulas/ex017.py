import math

catAd = float(input('Qual o valor do cateto adjacente? '))
catOp = float(input('Qual o valor do cateto oposto? '))
print('A hipotenusa é {:.2f}'.format(math.hypot(catOp, catAd)))