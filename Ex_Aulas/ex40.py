a = float(input('Digite a sua primeira nota? '))
b = float(input('Digite a sua segunda nota? '))
media = (a + b) / 2
print(media)
if media < 5.0:
    print('Reprovado')
elif media >= 5.0 and media <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')