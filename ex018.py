import math

ang = float(input("Digite o angulo: "))
angRad = math.radians(ang)
sen = math.sin(angRad)
cos = math.cos(angRad)
tan = math.tan(angRad)
print("Para o angulo {}, o cosseno {:.2f}, seno {:.2f} e tangente {:.2f}".format(ang, cos, sen, tan))
