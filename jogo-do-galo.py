import os

# Verifica se o jogo foi vencido
def Vitoria(situacaoJogo,jogadores):
    jogadorBola = []
    jogadorCruz = []
    for i in range(9):
        if situacaoJogo[i] == "O": # armazena as posições onde tem "O" 
            jogadorBola.append(i)
        if situacaoJogo[i] == "X": # armazena as posições onde tem "X"
            jogadorCruz.append(i)
    if len(jogadorCruz) > 2: # só começa a verificação se o jogador Cruz tiver ao menos 3 marcações
        if 0 in jogadorCruz:
            if 1 in jogadorCruz:
                if 2 in jogadorCruz:
                    return jogadores[1]
            if 3 in jogadorCruz:
                if 6 in jogadorCruz:
                    return jogadores[1]
            if 4 in jogadorCruz:
                if 8 in jogadorCruz:
                    return jogadores[1]
        if 1 in jogadorCruz:
            if 4 in jogadorCruz:
                if 7 in jogadorCruz:
                    return jogadores[1]
        if 2 in jogadorCruz:
            if 3 in jogadorCruz:
                if 6 in jogadorCruz:
                    return jogadores[1]
            if 5 in jogadorCruz:
                if 8 in jogadorCruz:
                    return jogadores[1]
        if 3 in jogadorCruz:
            if 4 in jogadorCruz:
                if 5 in jogadorCruz:
                    return jogadores[1]
        if 6 in jogadorCruz:
            if 7 in jogadorCruz:
                if 8 in jogadorCruz:
                    return jogadores[1]
    if len(jogadorBola) > 2: # só começa a verificação se o jogador Bola tiver ao menos 3 marcações
        if 0 in jogadorBola:
            if 1 in jogadorBola:
                if 2 in jogadorBola:
                    return jogadores[0]
            if 3 in jogadorBola:
                if 6 in jogadorBola:
                    return jogadores[0]
            if 4 in jogadorBola:
                if 8 in jogadorBola:
                    return jogadores[0]
        if 1 in jogadorBola:
            if 4 in jogadorBola:
                if 7 in jogadorBola:
                    return jogadores[0]
        if 2 in jogadorBola:
            if 3 in jogadorBola:
                if 6 in jogadorBola:
                    return jogadores[0]
            if 5 in jogadorBola:
                if 8 in jogadorBola:
                    return jogadores[0]
        if 3 in jogadorBola:
            if 4 in jogadorBola:
                if 5 in jogadorBola:
                    return jogadores[0]
        if 6 in jogadorBola:
            if 7 in jogadorBola:
                if 8 in jogadorBola:
                    return jogadores[0]
    return "O jogo não acabou"

def Tabuleiro(situacaoJogo): # executa o print do tabuleiro atualizado
    print ("\t%s\t|\t%s\t|\t%s\n\t%s\t|\t%s\t|\t%s\n\t%s\t|\t%s\t|\t%s" %(situacaoJogo[0],situacaoJogo[1],situacaoJogo[2],situacaoJogo[3],situacaoJogo[4],situacaoJogo[5],situacaoJogo[6],situacaoJogo[7],situacaoJogo[8]))

def OcuparCasa(situacaoJogo, numeroJogador, campoSelecionado): # modifica o jogo de acordo com a seleção feita pelo jogador
    if numeroJogador == 1:
        situacaoJogo.insert(campoSelecionado-1,"X") # troca a posição numerica por "X"
        del situacaoJogo[campoSelecionado]
    elif numeroJogador == 0:
        situacaoJogo.insert(campoSelecionado-1,"O") # troca a posição numerica por "O"
        del situacaoJogo[campoSelecionado]
    else:
        return situacaoJogo, False 
    
    return situacaoJogo

            

jogarNovamente = "S"
while jogarNovamente == "S": # vericar se o jogador quer jogar novamente
    situacaoJogo = ["1","2","3","4","5","6","7","8","9"] # posição das casas do jogo
    jogadores = [] # armazena o nome dos jogadores

    # adiciona os jogadores ao jogo
    for i in range(2):
        jogadores.append(input("Nome do jogador número " + str(i+1) + ":"))
    print ("Escolha um número da tabela")
    # while onde acontece o jogo
    i=0
    while i != 9: # FAZER O MENOS UM TA SENDO IGNORADO...........................................................................
        Tabuleiro(situacaoJogo)
        try:
            campoSelecionado = int(input("Vez de(a)" + jogadores[i%2] + ":")) # jogador seleciona onde quer jogar
            if str(campoSelecionado) not in situacaoJogo:
                i-=1
                os.system("cls")
                print("Já foi marcado, tente novamente")
            else:
                situacaoJogo = OcuparCasa(situacaoJogo, i%2, campoSelecionado) # atuzaliza a variavel situacaoJogo para as novas definições escolhidas pelo usuario

                vencedor = Vitoria(situacaoJogo, jogadores) # verifica se teve um vencerdor
                os.system("cls")
                if vencedor == jogadores[0]:
                    print("%s venceu!!!" %(jogadores[0]))
                    break
                elif vencedor == jogadores[1]:
                    print("%s venceu!!!" %(jogadores[1]))
                    break
                if i == 8:
                    print ("Empate")
        except ValueError:
            print("Valor invalido")
            i-=1
        i+=1

    jogarNovamente = input("Deseja jogar novamente (S/N): ")