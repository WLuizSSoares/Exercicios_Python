soma = 0
quantidade = 0
maior1000 = 0
produtos = []
while True:
    nome = str(input('Qual o nome do produto? ')).strip()
    preço = float(input('Qual o valor? '))
    produtos.append((nome, preço))

    if preço != 0:
        soma += preço
    if preço > 1000:
        maior1000 += 1

    cadastro = str(input('Continuar cadastrando? S/N ')).upper().strip()[0]
    while cadastro not in "SN":
        cadastro = str(input('Inválido, apenas S ou N: ')).upper().strip()[0]

    if cadastro == "N":
        break

print(f"\nO total gasto é R${soma}")
print(f"Temos {maior1000} produtos custamndo mais de R$1000.00 ")
mais_barato = min(produtos, key=lambda x: x[1])
print(f"O nome do produto mais barato é: {mais_barato[0]} (R${mais_barato[1]:.2f})")


