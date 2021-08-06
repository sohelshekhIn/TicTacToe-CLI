
# Tic Tac Toe CLI
Tic Tac Toe Game in Command Line Interface using python



## Runnig
```
py tic_tac_toe.py
```









# Code Explanation

## Game Logic

Step 1: Clears terminal and Prints Board

Step 2: Takes input from player

Step 3: Checks if input was valid input (i.e. an integer)

Step 4: Checks if input ranges from 1 to 9

Step 5: Checks if the input position is empty in Board

Step 6: Registers Move in the input position for the current player

Step 7: Runs Game Logic where it checks if any player Won

Step 8: If no Win / Loss, Goes to Step 1 for number of empty space in Board

Step 9: If Player Won / Match Draw, prints message and exits the programme




## Line by Line Explanation Of Code


Importing system function from os

Defining Global variables, which are to be accessed from anywhere in the file.
This includes, 

    positionalData - The value of player mves in board in form of an array

    player - Value of curernt player in form of s string

    playerX - Array to have all moves of player X

    playerO - Array to have all moves of player O

    winMatch - Boolean Value which tells if any player won match, True for no won

A clear() function to clear the terminal by running system("clear||cls")

A checkEmptyPos() function, which takes player-input as argument to check
if the move position if empty in boar (i.e. in positionalData). And returns 
True if empty and False if position not empty

A registerMove() function, which takes move-position and current player as arguments
to register the move for current player in board (i.e. in positionalData) and 
in array of specific player (i.e. either in array playerX or playerO)

A printBoard() function, which takes positional-datas as an optional argument,
and runs the clear() function to clear the terminal and prints the board using 
python multiline print statement (i.e. print(""" """))

A emptyDataSets() function, which sets value of differnt arrays (i.e. playerX, playerO
and positionalData) as empty, to reset value of previous match

A takeInput() function which - 
    Runs inside a foor loop for 9 time (if no win), then checks winMatch var 
    if any player won -
        If yes, then do not runs the takeInput() function anymore
        If no, then runs the function and checks if its an draw or not

    Takes player input and checks whether its not an empty input, not a string and is a integer only
    
    Checks if the input in in between 1 to 9
    
    Runs checkEmptyPos() function to check if position is empty - 
        If yes, then continues with remaining Code
        If no, then prints Enter another position, this position already occupied
        and re-runs takeInput() function
    
    If checkEmptyPos() returns True, then - 
    Runs registerMove() function with player-input and current player as argument and registers the players
    move

    Runs printBoard() funtion with new input positionalData as argument, for visual feedback
    of players' input

    Runs game logic and saves Value of it in a var checkGameLogic - 
        If checkGameLogic is equal to 0, then player X won
        If checkGameLogic is equal to 1, then player O won
        Else, changes currnt player from X to O or O to X

        If checkGameLogic was equal to 0 or 1 then prints message of that player won
        and ends the loops

A gameLogic() function which  takes current player as argument
    Has a array of arrays name winPosition, which contains all the position of winning chances
    defaultMatches - An array of 0 int values for length of 8
    winner - Var which will have value of player won (i.e. 0 or 1)

    If current player is equal to X then checks if array playerX contains positions 
    In winPosition -
        If yes, then checks all three values of moves ar in winPosition -
            If yes, then player X won
        If no, function ends

    And same goes for player O
    And returns 0 if player X won, 1 if player O won, and None if none player won


Then if name main statement ( A system reserved Vars ) - 
    This if statement checks if the file runnning name is equal to main
    The Code under this if statement runs only if this file is running, if the functions or Code
    under this statments are asked to run outside this file, it will not work.

    Under this,
        It Prints the board with welcomeData array, which tells what position is what

        Then a while loop runs (infinite) - 
            Asks if want to play the game, then press enter,
            Want to Exit the game, press q

            If input was Enter (i.e. Empty Input) then runs printBoard() and takeInput()
            If input was q then break is runs to exit the while loop and end the programme.

  
