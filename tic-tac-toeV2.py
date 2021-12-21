import random
import os


# Detecta se o jogo foi vencido por algum jogador
def WinningDetection(gameStatus, round):
    winningPossibilities = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]
    if round > 2: 
        if round%2 == 0:                                                #Verifica se o jogador 1 ganhou
            player1 = []
            for i in range(9):                                          #Verifica onde o jogador 1 já marcou
                if gameStatus[i] == "O":
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

# Cria uma imagem no terminal da situação atual do tabuleiro
def Board(gameStatus):
    print ("\t\t|\t\t|\n\t%s\t|\t%s\t|\t%s\n________________|_______________|________________\n\t\t|\t\t|\n\t%s\t|\t%s\t|\t%s\n________________|_______________|________________\n\t\t|\t\t|\n\t%s\t|\t%s\t|\t%s\n\t\t|\t\t|" %(gameStatus[0],gameStatus[1],gameStatus[2],gameStatus[3],gameStatus[4],gameStatus[5],gameStatus[6],gameStatus[7],gameStatus[8]))

# Marca a posição selecionada pelo jogador
def SelectPosition(gameStatus, player, numberSelected):
    if player == 1:
        gameStatus.insert(numberSelected-1,"X") # troca a posição numerica por "X"
        del gameStatus[numberSelected]
    elif player == 0:
        gameStatus.insert(numberSelected-1,"O") # troca a posição numerica por "O"
        del gameStatus[numberSelected]
    return gameStatus

# Uma função criada, para ver onde já foi marcado em uma possibilidade de vitoria e retorna a posição que ainda não foi marcada
def ElementsNotAreadyUsed(list,listToCompare):
    for i in range (len(listToCompare)):
        if listToCompare[i] not in list:
            return listToCompare[i]+1

# Funionamento da IA            
def AI(gameStatus,round):
    winningPossibilities1 = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]
    winningPossibilities2 = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]
    player1 = []
    player2 = []
    # Marca a situação de jogo do jogador "O" e jogador "X" em forma de motrar suas posições
    if round%2 != 0:
        for i in range(len(gameStatus)):
            if gameStatus[i] == "O":
                player1.append(i)
            if gameStatus[i] == "X":
                player2.append(i)
    else:
        for i in range(len(gameStatus)):
            if gameStatus[i] == "X":
                player1.append(i)
            if gameStatus[i] == "O":
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

# Modo de jogo contra a IA
def AIGame():
    gameStatus = ["1","2","3","4","5","6","7","8","9"] # posição das casas do jogo
    players=["AI"]
    flipCoin = random.randint(0,1)
    # Adiciona o jogador ao jogo
    players.insert(flipCoin,(input("Player name: ")))

    
    os.system("cls")
    print ("Select a number from the board: ")

    # While onde acontece o jogo
    round=0
    while round != 9:
        turn = 0
        if round%2 == 0:
            turn = players[0]
        else:
            turn = players[1]
        Board(gameStatus) # Print do tabuleiro
        try:
            # Vez jogador
            if turn != "AI":
                numberSelected = int(input("Round " + str(round+1) + "\n" + players[round%2] + "'s turn:")) # Jogador seleciona onde quer jogar
                if str(numberSelected) not in gameStatus and  numberSelected < 10:
                    round-=1
                    os.system("cls")
                    print("It's aready selected")
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
            #Vez IA
                numberSelected = AI(gameStatus,round) # IA toma decisão de valor que irá jogar
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
        except ValueError:
            print("Invalid value")
            round-=1
        except:
            print("Something is wrong!")
        round+=1


# Modo de jogo jogador vs jogador
def VsGame():
    gameStatus = ["1","2","3","4","5","6","7","8","9"] # posição das casas do jogo
    players=[]
    # Adiciona os jogadores ao jogo
    for i in range(2):
        players.append(input("Name of player " + str(i+1) + ": "))
    os.system("cls")
    while True:
        selectPlayer = input("Which player goes first?\n1 - %s\n2 - %s\n" %(players[0], players[1]))
        if selectPlayer in ["1","2"]:
            break
        else:
            os.system("cls")
            print("Select a valid input, pls!!!")
    if selectPlayer == "2":
        players.reverse()
    os.system("cls")
    print ("Select a number from the board")

    # While onde acontece o jogo
    round=0
    while round != 9:
        Board(gameStatus) #Print do mapa
        try:
            # Vez jogador "O"
            if round%2 == 0:
                numberSelected = int(input("Round " + str(round+1) + "\n" + players[round%2] + "'s turn:")) # Jogador seleciona onde quer jogar
                if str(numberSelected) not in gameStatus and  numberSelected < 10:
                    round-=1
                    os.system("cls")
                    print("It's aready selected")
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
            # Vez jogador "X"
                numberSelected = int(input("Round " + str(round+1) + "\n" + players[round%2] + "'s turn:")) # Jogador seleciona onde quer jogar
                if str(numberSelected) not in gameStatus and  numberSelected < 10:
                    round-=1
                    os.system("cls")
                    print("It's aready selected")
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
            print("Invalid value")
            round-=1
        except:
            print("Something is wrong!")
        round+=1

def Main():
    playAgain = True
    askPlayAgain = ""
    while playAgain != False:
        try:
            playAgainGameMode = True
            if askPlayAgain == "":
                selectMode = int(input("Which game mode do you wish to play?\n\n1 - Singleplayer\n2 - Multiplayer\n"))
            if selectMode == 1:
                while playAgainGameMode != False:
                    os.system("cls")
                    print("AI game mode!")
                    AIGame()
                    askPlayAgainGameMode = input("Do you want to play vs AI again? (Y/N):")
                    if askPlayAgainGameMode.upper() != "Y":
                        playAgainGameMode = False
            elif selectMode == 2:
                while playAgainGameMode != False:
                    os.system("cls")
                    print("Vs game mode!")
                    VsGame()
                    askPlayAgainGameMode = input("Do you want to play vs another player again? (Y/N):")
                    if askPlayAgainGameMode.upper() != "Y":
                        playAgainGameMode = False
            os.system("cls")  
            askPlayAgain = input("Do you want to play Tic-Tac-Toe again? (Y/N):")
            if askPlayAgain.upper() != "Y":
                playAgain = False
            else:
                if selectMode == 1:
                    selectMode = 2
                elif selectMode == 2:
                    selectMode = 1
        except ValueError:
            os.system("cls")
            print("Invalid value. Try again!")
        except:
            os.system("cls")
            print("Something is wrong!")

os.system("cls")
Main()