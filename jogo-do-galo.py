import os
import random

def VitoriaV2(situacaoJogo,jogadores):
    vitoria = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,4,7],[2,5,8],[3,4,5],[6,7,8]]
    jogadorBola = []
    jogadorCruz = []
    for i in range(9):
        if situacaoJogo[i] == chr(216): # armazena as posições onde tem "O" 
            jogadorBola.append(i)
        if situacaoJogo[i] == "X": # armazena as posições onde tem "X"
            jogadorCruz.append(i)
    if len(jogadorBola) > 2:
        for i in range(len(vitoria)):
            possuiUmValorBola = 0
            possuiUmValorCruz = 0
            for j in range(len(vitoria[i])):
                if vitoria[i][j] in jogadorBola:
                    possuiUmValorBola+=1
                    if possuiUmValorBola == len(vitoria[i]):
                        return jogadores[0]
                if vitoria[i][j] in jogadorCruz:
                    possuiUmValorCruz+=1
                    if possuiUmValorCruz == len(vitoria[i]):
                        return jogadores[1]
    return "O jogo não acabou"








# Verifica se o jogo foi vencido
def Vitoria(situacaoJogo,jogadores):
    jogadorBola = []
    jogadorCruz = []
    for i in range(9):
        if situacaoJogo[i] == chr(216): # armazena as posições onde tem "O" 
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
    print ("\t\t|\t\t|\n\t%s\t|\t%s\t|\t%s\n________________|_______________|________________\n\t\t|\t\t|\n\t%s\t|\t%s\t|\t%s\n________________|_______________|________________\n\t\t|\t\t|\n\t%s\t|\t%s\t|\t%s\n\t\t|\t\t|" %(situacaoJogo[0],situacaoJogo[1],situacaoJogo[2],situacaoJogo[3],situacaoJogo[4],situacaoJogo[5],situacaoJogo[6],situacaoJogo[7],situacaoJogo[8]))

def OcuparCasa(situacaoJogo, numeroJogador, campoSelecionado): # modifica o jogo de acordo com a seleção feita pelo jogador
    if numeroJogador == 1:
        situacaoJogo.insert(campoSelecionado-1,"X") # troca a posição numerica por "X"
        del situacaoJogo[campoSelecionado]
    elif numeroJogador == 0:
        situacaoJogo.insert(campoSelecionado-1,chr(216)) # troca a posição numerica por "O"
        del situacaoJogo[campoSelecionado]
    else:
        return situacaoJogo, False 
    
    return situacaoJogo

def removerElementoNaoPertencente(lista,listaComparar):
    for i in range (len(listaComparar)):
        if listaComparar[i] not in lista:
            return listaComparar[i]+1



def IA(situacaoJogo):
    vitoria = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,4,7],[2,5,8],[3,4,5],[6,7,8]]
    jogadorBola = []
    jogadorCruz = []
    for i in range(len(situacaoJogo)):
        if situacaoJogo[i] == chr(216):
            jogadorBola.append(i)
        if situacaoJogo[i] == "X":
            jogadorCruz.append(i)
    for i in range(len(vitoria)):
        for j in range(len(vitoria[i])):
            if vitoria[i][j] in jogadorCruz:
                vitoria[i].clear()
                break
    for i in range(len(vitoria)):
        possuiUmValor = 0
        for j in range(len(vitoria[i])):
            if vitoria[i][j] in jogadorBola:
                possuiUmValor+=1
            if possuiUmValor > 1:
                return removerElementoNaoPertencente(jogadorBola,vitoria[i])
    infinito = True
    while infinito != False:
        jogadaAleatoria = random.randint(1,9)
        if jogadaAleatoria not in situacaoJogo:
            return jogadaAleatoria


os.system("cls")
jogarNovamente = "S"
while jogarNovamente == "S": # vericar se o jogador quer jogar novamente
    situacaoJogo = ["1","2","3","4","5","6","7","8","9"] # posição das casas do jogo
    jogadores=["IA"]
    
    # adiciona os jogadores ao jogo
    jogadores.insert(0,(input("Nome do jogador: ")))
    
    os.system("cls")
    print ("Escolha um número da tabela")
    # while onde acontece o jogo
    rodada=0
    while rodada != 9:
        Tabuleiro(situacaoJogo)
        try:
            if rodada%2 == 0:
                campoSelecionado = int(input("Vez de(a)" + jogadores[rodada%2] + ":")) # jogador seleciona onde quer jogar
                if str(campoSelecionado) not in situacaoJogo and  campoSelecionado < 10:
                    rodada-=1
                    os.system("cls")
                    print("Já foi marcado, tente novamente")
                elif campoSelecionado > 10:
                    rodada-=1
                    os.system("cls")
                    print("Valor invalido!")
                else:
                    situacaoJogo = OcuparCasa(situacaoJogo, rodada%2, campoSelecionado) # atuzaliza a variavel situacaoJogo para as novas definições escolhidas pelo usuario

                    vencedor = VitoriaV2(situacaoJogo, jogadores) # verifica se teve um vencerdor
                    os.system("cls")
                    if vencedor == jogadores[0]:
                        Tabuleiro(situacaoJogo)
                        print("%s venceu!!!" %(jogadores[0]))
                        break
                    elif vencedor == jogadores[1]:
                        Tabuleiro(situacaoJogo)
                        print("%s venceu!!!" %(jogadores[1]))
                        break
                    if rodada == 8:
                        Tabuleiro(situacaoJogo)
                        print ("Empate")
            else:
                campoSelecionado = IA(situacaoJogo)
                if str(campoSelecionado) not in situacaoJogo and  campoSelecionado < 10:
                    rodada-=1
                    os.system("cls")
                    print("Já foi marcado, tente novamente")
                elif campoSelecionado > 10:
                    rodada-=1
                    os.system("cls")
                    print("Valor invalido!")
                else:
                    situacaoJogo = OcuparCasa(situacaoJogo, rodada%2, campoSelecionado) # atuzaliza a variavel situacaoJogo para as novas definições escolhidas pelo usuario

                    vencedor = VitoriaV2(situacaoJogo, jogadores) # verifica se teve um vencerdor
                    os.system("cls")
                
                    if vencedor == jogadores[0]:
                        Tabuleiro(situacaoJogo)
                        print("%s venceu!!!" %(jogadores[0]))
                        break
                    elif vencedor == jogadores[1]:
                        Tabuleiro(situacaoJogo)
                        print("%s venceu!!!" %(jogadores[1]))
                        break
        except ValueError:
            print("Valor invalido")
            rodada-=1
        rodada+=1














'''         
os.system("cls")
jogarNovamente = "S"
while jogarNovamente == "S": # vericar se o jogador quer jogar novamente
    situacaoJogo = ["1","2","3","4","5","6","7","8","9"] # posição das casas do jogo
    jogadores = [] # armazena o nome dos jogadores

    # adiciona os jogadores ao jogo
    for i in range(2):
        jogadores.append(input("Nome do jogador número " + str(i+1) + ":"))
    os.system("cls")
    print ("Escolha um número da tabela")
    
    
    # while onde acontece o jogo
    rodada=0
    while rodada != 9:
        Tabuleiro(situacaoJogo)
        try:
            campoSelecionado = int(input("Vez de(a)" + jogadores[rodada%2] + ":")) # jogador seleciona onde quer jogar
            if str(campoSelecionado) not in situacaoJogo and  campoSelecionado < 10:
                rodada-=1
                os.system("cls")
                print("Já foi marcado, tente novamente")
            elif campoSelecionado > 10:
                rodada-=1
                os.system("cls")
                print("Valor invalido!")
            else:
                situacaoJogo = OcuparCasa(situacaoJogo, rodada%2, campoSelecionado) # atuzaliza a variavel situacaoJogo para as novas definições escolhidas pelo usuario

                vencedor = Vitoria(situacaoJogo, jogadores) # verifica se teve um vencerdor
                os.system("cls")
                if vencedor == jogadores[0]:
                    Tabuleiro(situacaoJogo)
                    print("%s venceu!!!" %(jogadores[0]))
                    break
                elif vencedor == jogadores[1]:
                    Tabuleiro(situacaoJogo)
                    print("%s venceu!!!" %(jogadores[1]))
                    break
                if rodada == 8:
                    Tabuleiro(situacaoJogo)
                    print ("Empate")
        except ValueError:
            print("Valor invalido")
            rodada-=1
        rodada+=1

    jogarNovamente = input("Deseja jogar novamente (S/N): ")
'''