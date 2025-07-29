salario = float(input('Qual o valor do seu salário? '))
if salario > 1250.00:
    aumento = (salario * 10) / 100
    print('O aumento do seu salário é R${}, se tornando R${}'.format(aumento, salario+aumento))
else:
    aumento2 = (salario * 15) / 100
    print('O aumento do seu salário é de R${}, se tornando R${}'.format(aumento2, aumento2+salario))