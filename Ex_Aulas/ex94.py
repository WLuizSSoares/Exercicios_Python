cadastro = list()
while True:
    pessoas = dict()
    pessoas['nome'] = str(input("Nome: "))
    while True:
        pessoas['sexo'] = str(input("Sexo: (M/F) ")).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro!, Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input("Idade: "))
    cadastro.append(pessoas.copy())
    while True:
        condicao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if condicao in ["S", "N"]:
            break
        else:
            print("Resposta inválida!, Por favor, digite apenas 'S' para sim e 'N' para não")
    if condicao == "N":
        break
print('-='*30)
#1. Cálculo da soma e média
somaIdades = 0
for p in cadastro:
    somaIdades += p['idade']
total_pessoas = len(cadastro)
if total_pessoas > 0:
    media = somaIdades / len(cadastro)
    print(f'- Foram cadastradas {total_pessoas} pessoas.')
    print(f'- A média de idade do grupo é de {media:.2f} anos. ')
    #2. Lista de mulheres
    mulheres = list()
    for pessoas in cadastro:
        if pessoas['sexo'] == "F":
            mulheres.append(pessoas['nome'])
    print('- As mulheres cadastradas são:', end="")
    for nome in mulheres:
        print(f' {nome}', end="")
    print()
    #3. Lista de pessoas acima da media
    print(f'Lista de pessoas acima da média:')
    print()
    for p in cadastro:
        if p['idade'] > media:
            print(f"- Nome: {p['nome']} com {p['idade']} anos")
else:
    print('Nenhuma pessoa foi cadastrada')
print('<<encerrado>>')
