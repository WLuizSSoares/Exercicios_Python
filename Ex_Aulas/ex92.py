from datetime import datetime
pessoa = dict()
cadastro = list()
pessoa["nome"] = str(input('Nome: '))
pessoa["nascimento"] = int(input('Ano de nascimento: '))
pessoa["carteira_de_trabalho"] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa["carteira_de_trabalho"] != 0:
    pessoa["ano_de_contratacao"] = int(input('Ano de contratação: '))
    pessoa["salario"] = float(input('Salário: '))
    aposentadoria = (pessoa["ano_de_contratacao"] + 35) - pessoa["nascimento"]
cadastro.append(pessoa.copy())
print('-=' *30)  
print(f'Nome tem o valor {pessoa["nome"]}')
print(f'Idade tem o valor {(datetime.now().year - pessoa["nascimento"])}')
if pessoa["carteira_de_trabalho"] == 0:
    print(f'Ctps tem o valor {pessoa["carteira_de_trabalho"]}')
else:
    print(f'Ctps tem o valor igual a {pessoa["carteira_de_trabalho"]}')
    print(f'Contratação tem o valor {pessoa["ano_de_contratacao"]}')
    print(f'Salario tem o valor {pessoa["salario"]}')
    print(f'Aposentadoria tem o valor {aposentadoria}')