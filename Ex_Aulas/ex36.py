valorCasa = float(input('\033[7;40mQual o valor da casa? R$'))
salario = float(input('\033[7;40mQual o valor do seu salário? R$'))
anos = float(input('\033[7;40mEm quantos anos você pretende pagar?'))
prestacaoMensal= (valorCasa / anos) / 12
taxaLimite = (salario * 30) / 100
if prestacaoMensal <= taxaLimite:
    print('-=-'*20)
    print('O seu empréstimo foi aprovado!!!')
    print('O valor da sua prestação mensal é de: R${:.2f}'.format(prestacaoMensal))
    print('-=-'*20)
else:
    print(':( /' *10)
    print('Seu empréstimo foi negado!')
    print('O valor da parcela mensal R${:.2f}, é maior que 30% do seu salário de {}.\033[m'.format(prestacaoMensal, salario))