jogadores = list()
#1 Loop inicial de cadastro
while True:
    #1.1 - A cada loop do while, um novo dicionário Jogador é iniciado.
    jogador = dict()
    jogador['nome'] = str(input("Nome do jogador: "))
    jogador['partidas'] = int(input("Quantas partidas jogadas: "))
    # 2 - A chave 'gols' recebe como valor uma lista
    jogador['gols'] = list()
    #2.1 Condição para a criação do item partidas do dicionário.
    if jogador['partidas'] > 0:
        #3 Iteração de 'gols' relacionado a quantidade de partidas.
        for c in range(1, jogador['partidas']+1):
            numeroGols = int(input(f"Quantos gols na partida {c}? "))
            #4 Adição do numero de gols a lista dentro da chave 'gols'.
            jogador['gols'].append(numeroGols)
    else:
        print('Não houve partidas, não há gols para calcular')
    #5 Criação da chave 'total' com a soma do número de 'gols'.
    jogador['total'] = sum(jogador['gols'])
    #6 Copiando o dicionário único de cada jogador para uma lista contendo todos os jogadores.
    jogadores.append(jogador.copy())
    #7 Loop para condição de continuar cadastrando.
    while True:
        condicao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if condicao in ["S", "N"]:
            break
        else:
            print("Resposta inválida!, Por favor, digite apenas 'S' para sim e 'N' para não")
    if condicao == "N":
            break
print('-='*30)
#8 Visualização dos detalhes de cada jogador.
print(f'|{"cod":^4}{"nome":<15}|{"gols":<10}|{"total":<5}|')
print('-'*30)
for i, jogador in enumerate(jogadores):
    nome = jogador['nome']
    gols = str(jogador['gols'])
    total = jogador['total']

    print(f'|{i:^4}{nome:<15}|{gols:<10}|{total:>5}|')
print('-='*30)
# Bloco de consulta
while True:
    cod = int(input("Mostrar dados de qual jogador? 999 para parar "))
    if cod == 999:
        break
    if 0 <= cod < len(jogadores):
        jogadorSelecionado = jogadores[cod]
        print(f' --  Levantamento do jogador {jogadorSelecionado['nome']}')
        for i, gols in enumerate(jogadorSelecionado['gols']):
            print(f'  No jogo {i+1}, fez {gols} gols.')
    else:
        print("Erro, código de jogador inválido.")
print("Consulta finalizada. Até mais!")

