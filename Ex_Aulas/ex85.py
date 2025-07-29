princ = []
par = []
imp = []
for p in range(0,7):
    num = (int(input('Número: ')))
    if num %2 == 0:
        par.append(num)
    else:
        imp.append(num)
par.sort()
imp.sort()
princ.append(par)
princ.append(imp)

print(f'Valores pares: {princ[0]}')
print(f'Valores impares: {princ[1]}')

