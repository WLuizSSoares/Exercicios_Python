sexo = str(input('Qual o seu sexo? [M/F]: ')).strip().upper()
while sexo not in ['M', 'F']:
    print('Sexo inválido,digite apenas M para masculino ou F para feminino!')
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
print("Sexo registrado!!")
