aluno = dict()
aluno["nome"] = str(input('Nome: '))
aluno["media"] = float(input(f'Media de {aluno["nome"]}: '))
print(f'Nome é igual a {aluno["nome"]}')
print(f'Media é igual a {aluno["media"]}')
if aluno["media"] >= 7.0:
    aluno["situação"] = 'Aprovado'
elif 5 <= aluno["media"] <7:
    aluno["situação"] = 'Recuperação'
else:
    aluno["situação"] = 'Reprovado'
print(aluno)