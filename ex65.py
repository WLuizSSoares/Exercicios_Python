r = "S"
soma = 0
media = 0
quantidade = 0
maior = menor = None
while r == "S":
    n =int(input('Digite um número inteiro: '))
    r = str(input('Quer continuar? S/N: ')).upper().strip() [0]
    soma += n
    quantidade += 1
    if maior is None or n > maior:
        maior = n
    elif menor is None or n < menor:
        menor = n

media = soma / quantidade
print('A média entre os números é {:.2f}'.format(media))
print('O maior número é {} e o menor número é {}'.format(maior, menor))
