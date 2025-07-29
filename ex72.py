n = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
user = int(input("Digite um número de 0 a 20: "))
while user < 0 or user > 20:
    user = int(input('Tente novamente, digite um numero entre 0 e 20: '))

print(n[user])