''' 
----------------------------
Tick Tack Toe
----------------------------
'''

game_positions = [" "," "," "," "," "," "," "," "," "]

def game_rules():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("WELCOME TO TICK TAC TOE!\n")
    print("HOW TO PLAY:")
    print("When it's your turn, you will be asked to enter the\nnumber that cooresponds with the location you wish to claim.")
    print("\nGAME BOARD LOCATIONS:")
    print("\t|\t|\n    7   |   8   |    9   \n\t|\t|\n------------------------\n\t|\t|\n    4   |   5   |    6   \n\t|\t|\n------------------------\n\t|\t|\n    1   |   2   |    3   \n\t|\t|\n")

def redraw():
        print(f"\t|\t|\n    {game_positions[6]}   |   {game_positions[7]}   |    {game_positions[8]}   \n\t|\t|\n------------------------\n\t|\t|\n    {game_positions[3]}   |   {game_positions[4]}   |    {game_positions[5]}   \n\t|\t|\n------------------------\n\t|\t|\n    {game_positions[0]}   |   {game_positions[1]}   |    {game_positions[2]}   \n\t|\t|\n")

def enter_position(playername):
    position = int(input(f"Player {playername} pick your square.  "))
    if position not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        print("That square does not exist. Please try again.")
        enter_position(playername)
    elif game_positions[position-1] == " ":
        game_positions[position-1] = playername
    else:
        print("That square is already played. Please try again.")
        enter_position(playername)

def replay():
    playagain = input("Would you like to play again? Enter Y for Yes and N for No.   ").upper()
    if playagain == "Y":
        game_positions[0] = " "
        game_positions[1] = " "
        game_positions[2] = " "
        game_positions[3] = " "
        game_positions[4] = " "
        game_positions[5] = " "
        game_positions[6] = " "
        game_positions[7] = " "
        game_positions[8] = " "
        redraw()
        playgame(player1char)
    else: 
        print("Goodbye!")

def check_for_win(playername):
    checkspace = " "
    if ((playername == game_positions[0] == game_positions[1] == game_positions[2]) or 
    (playername == game_positions[3] == game_positions[4] == game_positions[5]) or
    (playername == game_positions[6] == game_positions[7] == game_positions[8]) or
    (playername == game_positions[6] == game_positions[3] == game_positions[0]) or
    (playername == game_positions[7] == game_positions[4] == game_positions[1]) or
    (playername == game_positions[8] == game_positions[5] == game_positions[2]) or
    (playername == game_positions[8] == game_positions[4] == game_positions[0]) or
    (playername == game_positions[6] == game_positions[4] == game_positions[2])):
        print(f"Player {playername} Wins!")
        return True
    elif checkspace not in game_positions:
        print("No Winner!!")
        return True
    else:
        return False

def playgame(player1char):
    keepplaying = True
    player2char = " "
    if player1char == "X":
        player2char = "O"
    else:
        player2char = "X"

    while keepplaying:
        #Keep playing until someone loses
        enter_position(player1char)
        redraw()
        win = check_for_win(player1char)
        if win == True:
            break
        else:
            enter_position(player2char)
            redraw()
            win = check_for_win(player2char)
        if win == True:
            break


    #Ask if they wish to replay
    replay()


game_rules()
player1char = " "
while player1char != "X" and player1char != "O":
    player1char = input("Player 1: Would you like to be X or O?   ").upper()

playgame(player1char)