from os import system

# Global Vars
positionalData = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player = "X"
playerX = []
playerO = []
winMatch = True


def clear():
    """Clears the current terminal
    """
    system("clear||cls")


def checkEmptyPos(playerInput):
    """Checks if the given position from player is empty or not

    Args:
        player_input (int): The position where player wants to register the move

    Returns:
        boolean: Returns True if position is empty or Flase for occupied
    """
    playerInput = playerInput - 1
    if positionalData[playerInput] == " ":
        return True
    else:
        return False


def registerMove(movePosition, player):
    """Registers Move for player in general array (i.e. positionalData) and to playerX and playerO for Player X and Player O respectively

    Args:
        movePosition (int): Takes which position the player wants to enter
        player (string): The Current player who played the move
    """
    movePosition = movePosition - 1  # As array index starts from 0
    positionalData[movePosition] = player
    if player == "X":
        playerX.append(movePosition)
    else:
        playerO.append(movePosition)


# Prints Board in the terminal
def printBoard(positionalDatas=positionalData):
    """Clears existting terminal data and prints board with values from positionalDatas

    Args:
        positional_Datas (array, optional): Takes optional input for printing that data in board. Defaults to positional_Data.
    """
    clear()
    print(f"""

        Tic Tac Toe Game
            by Sohel


          |       |
      {positionalDatas[0]}   |   {positionalDatas[1]}   |  {positionalDatas[2]}
    ______|_______|______
          |       |
      {positionalDatas[3]}   |   {positionalDatas[4]}   |  {positionalDatas[5]}
    ______|_______|______
          |       |
      {positionalDatas[6]}   |   {positionalDatas[7]}   |  {positionalDatas[8]}
          |       |
          """)


def emptyDataSets():
    """Clears data from all the arrays for new game session
    """
    global playerO, playerX, positionalData
    playerX = []
    playerO = []
    positionalData = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def takeInput():
    """Runs in loop for 9 chances, takes input, validates it and passes to registerMove and Game Logic
    """
    global player, winMatch
    for i in range(9):
        if winMatch:
            while True:
                try:
                    playerInput = int(input(f"Enter position ({player}): "))
                    if playerInput >= 1 and playerInput <= 9:
                        if checkEmptyPos(playerInput):
                            registerMove(playerInput, player)
                            printBoard(positionalData)
                            checkGameLogic = gameLogic(player)
                            if checkGameLogic == 0:
                                print("""
    -----Player X Won----
    """)
                                emptyDataSets()
                                break
                            elif checkGameLogic == 1:
                                print("""
    -----Player O Won-----
    """)
                                emptyDataSets()
                                break
                            else:
                                if player == "X":
                                    player = "O"
                                elif player == "O":
                                    player = "X"
                            break
                        else:
                            print("Position Occupied, Enter another position!")
                    else:
                        print("Enter position input ranging 1-9")
                except ValueError as e:
                    print("Empty Field, String or Float Number not allowed!")
            if i == 8 and winMatch:
                print("""
    ------Match Draw-----
    """)
                emptyDataSets()


def gameLogic(player):
    """Checks all the moves from playerX and playerO arrays, if any contains any
    win moves, if yes then returns winner as 0 for player X and 1 for player O or returns None 
    for no win, loss

    Args:
        player (String): Takes current player to check if the current player won or loss

    Returns:
        int: Returns 
            0 if player X Won
            1 if player O Won
            None if none of the one won
    """
    global winMatch
    winPosition = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
        0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    defaulMatches = [0, 0, 0, 0, 0, 0, 0, 0]
    winner = None
    matchX, matchO = defaulMatches, defaulMatches
    if player == "X":
        for i in range(len(playerX)):
            for j in range(len(winPosition)):
                if playerX[i] in winPosition[j]:
                    matchX[j] += 1

        for k in range(len(matchX)):
            if matchX[k] == 3:
                winner = 0
                winMatch = False
    else:
        for i in range(len(playerO)):
            for j in range(len(winPosition)):
                if playerO[i] in winPosition[j]:
                    matchO[j] += 1

        for k in range(len(matchX)):
            if matchO[k] == 3:
                winner = 1
                winMatch = False
    matchX, matchO = defaulMatches, defaulMatches
    return winner


if __name__ == "__main__":
    welcomeData = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    printBoard(welcomeData)
    while True:
        print("""
    Press Enter to play
    Press q to exit
""")
        cmd = input()
        if cmd == "":
            emptyDataSets()
            printBoard()
            takeInput()
        elif cmd == "q":
            break
