import random
import os


#Detecta se o jogo foi vencido
def WinningDetection(gameStatus, round):
    winningPossibilities = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]
    if round > 2: 
        if round%2 == 0:                                                #Verifica se o jogador 1 ganhou
            player1 = []
            for i in range(9):                                          #Verifica onde o jogador 1 já marcou
                if gameStatus[i] == chr(216):
                    player1.append(i)
            for i in range(len(winningPossibilities)):
                winPlayer1 = 0
                for j in range(len(winningPossibilities[i])):
                    if winningPossibilities[i][j] in player1:
                        winPlayer1 +=1
                if winPlayer1 == 3:                                     #Se o jogador tiver as 3 marcações de possibilidade de winningPossibilities returna 1 (pela lista que possui os nomes q eu estou utilizando)
                    return 0             
        else:                                                           #Verifica se o jogador 2 ganhou
            player2 = []
            for i in range(9):
                if gameStatus[i] == "X":                                #Verifica onde o jogador 2 já marcou
                    player2.append(i)
            for i in range(len(winningPossibilities)):
                winPlayer2 = 0
                for j in range(len(winningPossibilities[i])):
                    if winningPossibilities[i][j] in player2:
                        winPlayer2 +=1
                if winPlayer2 == 3:                                     #Se o jogador tiver as 3 marcações de possibilidade de winningPossibilities returna 1 (pela lista que possui os nomes q eu estou utilizando)
                    return 1
    return "The game is not over yet"

def Board(gameStatus): # executa o print do tabuleiro atualizado
    print ("\t\t|\t\t|\n\t%s\t|\t%s\t|\t%s\n________________|_______________|________________\n\t\t|\t\t|\n\t%s\t|\t%s\t|\t%s\n________________|_______________|________________\n\t\t|\t\t|\n\t%s\t|\t%s\t|\t%s\n\t\t|\t\t|" %(gameStatus[0],gameStatus[1],gameStatus[2],gameStatus[3],gameStatus[4],gameStatus[5],gameStatus[6],gameStatus[7],gameStatus[8]))

def SelectPosition(gameStatus, player, numberSelected):
    if player == 1:
        gameStatus.insert(numberSelected-1,"X") # troca a posição numerica por "X"
        del gameStatus[numberSelected]
    elif player == 0:
        gameStatus.insert(numberSelected-1,chr(216)) # troca a posição numerica por "O"
        del gameStatus[numberSelected]
    return gameStatus

def ElementsNotAreadyUsed(list,listToCompare):
    for i in range (len(listToCompare)):
        if listToCompare[i] not in list:
            return listToCompare[i]+1


def IA(gameStatus):
    winningPossibilities1 = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,4,7],[2,5,8],[3,4,5],[6,7,8]]
    winningPossibilities2 = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,4,7],[2,5,8],[3,4,5],[6,7,8]]
    player1 = []
    player2 = []
    for i in range(len(gameStatus)):
        if gameStatus[i] == chr(216):
            player1.append(i)
        if gameStatus[i] == "X":
            player2.append(i)

    # IA tenta ganhar
    #Remove onde o jogador 1 impede a IA de ganhar
    for i in range(len(winningPossibilities1)):
        for j in range(len(winningPossibilities1[i])):
            if winningPossibilities1[i][j] in player1:
                winningPossibilities1[i].clear()
                break
    # Verifica onde existe alguma possibilidade de vitoria
    for i in range(len(winningPossibilities1)):
        winPlayer2 = 0
        for j in range(len(winningPossibilities1[i])):
            if winningPossibilities1[i][j] in player2:
                winPlayer2 +=1
        if winPlayer2 == 2:
            return ElementsNotAreadyUsed(player2,winningPossibilities1[i])

    # IA tenta não deixar jogador ganhar
    for i in range(len(winningPossibilities2)):
        for j in range(len(winningPossibilities2[i])):
            if winningPossibilities2[i][j] in player2:
                winningPossibilities2[i].clear()
                break
    for i in range(len(winningPossibilities2)):
        winPlayer1 = 0
        for j in range(len(winningPossibilities2[i])):
            if winningPossibilities2[i][j] in player1:
                winPlayer1+=1
        if winPlayer1 > 1:
            return ElementsNotAreadyUsed(player1,winningPossibilities2[i])
    
    # IA joga um valor aleatorio
    infinity = True
    while infinity != False:
        randomSelect = random.randint(1,9)
        if str(randomSelect) in gameStatus:
            return randomSelect


def IAGame():
    gameStatus = ["1","2","3","4","5","6","7","8","9"] # posição das casas do jogo
    players=["IA"]
    
    # Adiciona o jogador ao jogo
    players.insert(0,(input("Nome do jogador: ")))
    
    os.system("cls")
    print ("Escolha um número da tabela")

    # While onde acontece o jogo
    round=0
    while round != 9:
        Board(gameStatus) #Print do mapa
        try:
            if round%2 == 0:
                numberSelected = int(input("Time " + players[round%2] + ":")) # Jogador seleciona onde quer jogar
                if str(numberSelected) not in gameStatus and  numberSelected < 10:
                    round-=1
                    os.system("cls")
                    print("Is aready selected")
                elif numberSelected > 10:
                    round-=1
                    os.system("cls")
                    print("Invalid value")
                else:
                    gameStatus = SelectPosition(gameStatus, round%2, numberSelected) # Atuzaliza a variavel gameStatus para as novas definições escolhidas pelo usuario

                    winner = WinningDetection(gameStatus, round) # Verifica se teve um vencerdor
                    os.system("cls")
                    if winner == 0 or winner == 1:
                        Board(gameStatus)
                        print("%s wins!!!" %(players[winner]))
                        break
                    if round == 8:
                        Board(gameStatus)
                        print ("Draw")
            else:
                numberSelected = IA(gameStatus) # IA toma decisão de valor que irá jogar
                gameStatus = SelectPosition(gameStatus, round%2, numberSelected) # Atuzaliza a variavel gameStatus para as novas definições escolhidas pelo usuario

                winner = WinningDetection(gameStatus, round) # Verifica se teve um vencerdor
                os.system("cls")
            
                if winner == 0 or winner == 1:
                    Board(gameStatus)
                    print("%s wins!!!" %(players[winner]))
                    break
        except ValueError:
            print("Invalid value")
            round-=1
        round+=1


def VsGame():
    gameStatus = ["1","2","3","4","5","6","7","8","9"] # posição das casas do jogo
    players=[]
    
    # Adiciona os jogadores ao jogo
    for i in range(2):
        players.append(input("Nome do jogador " + str(i+1) + ": "))
    
    os.system("cls")
    print ("Escolha um número da tabela")

    # While onde acontece o jogo
    round=0
    while round != 9:
        Board(gameStatus) #Print do mapa
        try:
            if round%2 == 0:
                numberSelected = int(input("Time " + players[round%2] + ":")) # Jogador seleciona onde quer jogar
                if str(numberSelected) not in gameStatus and  numberSelected < 10:
                    round-=1
                    os.system("cls")
                    print("Is aready selected")
                elif numberSelected > 10:
                    round-=1
                    os.system("cls")
                    print("Invalid value")
                else:
                    gameStatus = SelectPosition(gameStatus, round%2, numberSelected) # Atuzaliza a variavel gameStatus para as novas definições escolhidas pelo usuario

                    winner = WinningDetection(gameStatus, round) # Verifica se teve um vencerdor
                    os.system("cls")
                    if winner == 0 or winner == 1:
                        Board(gameStatus)
                        print("%s wins!!!" %(players[winner]))
                        break
                    if round == 8:
                        Board(gameStatus)
                        print ("Draw")
            else:
                numberSelected = int(input("Time " + players[round%2] + ":")) # Jogador seleciona onde quer jogar
                if str(numberSelected) not in gameStatus and  numberSelected < 10:
                    round-=1
                    os.system("cls")
                    print("Is aready selected")
                elif numberSelected > 10:
                    round-=1
                    os.system("cls")
                    print("Invalid value")
                else:
                    gameStatus = SelectPosition(gameStatus, round%2, numberSelected) # Atuzaliza a variavel gameStatus para as novas definições escolhidas pelo usuario

                    winner = WinningDetection(gameStatus, round) # Verifica se teve um vencerdor
                    os.system("cls")
                    if winner == 0 or winner == 1:
                        Board(gameStatus)
                        print("%s wins!!!" %(players[winner]))
                        break
        except ValueError:
            print("Valor invalido")
            round-=1
        round+=1

IAGame()