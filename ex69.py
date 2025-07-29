contadoridade = contadormasculino = contadorfeminino = 0
while True:
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual o sexo? M/F ')).strip().upper()[0]
    while sexo not in "MF":
        sexo = str(input('Inválido, apenas M/F ')).upper().strip()[0]

    if idade > 18:
        contadoridade += 1
    if sexo == 'M':
        contadormasculino += 1
    if sexo == 'F':
        if idade < 20:
            contadorfeminino += 1

    cadastro = str(input('Quer continuar cadastrando? [S/N] ')).strip().upper()[0]
    while cadastro not in "SN":
        cadastro = str(input('Inválido, apenas S/N ')).strip().upper()[0]
    print('=-'*30)
    if cadastro != 'S':
        break

print(f'\n{contadoridade} tem mais de 18 anos')
print(f'Foram cadastrados {contadormasculino} homens.')
print(f'Foram cadastradas {contadorfeminino} mulheres abaixo de 20 anos')
print('fim')