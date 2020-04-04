import random

play = True

# Rock = 1:
# Paper = 2:
# Sissors =3

print("Let's play a game! Rock, Paper, Scissors")
print("1: Rock, 2:Paper, 3:Scissors, 4:Exit")
while play:
    computerpick = random.randint(1, 3)
    myhand = int(input("What do you want to throw: "))
    if myhand == 4:
        break
    while myhand > 3:
          myhand = int(input("Throw again: "))  
          if myhand == 4:
              play = False
              break
    if computerpick == myhand:
        print("Tie. Let's Play Again")
    # Computer Rock
    elif computerpick == 1 and myhand == 3:
        print("Computer threw Rock and beats your Sissors")
        print("Let's play again!")
    # Computer Paper
    elif computerpick == 2 and myhand == myhand == 1:
        print("Computer threw Paper and beats your Rock")
        print("Let's play again!")
    # computer Scissors
    elif computerpick == 3 and myhand == myhand == 2:
        print("Computer threw Scissors and beats your Paper")
        print("Let's play again!")
    elif myhand == 1 and computerpick ==3:
        print("You threw Rock and beat the Sissors of the computer")
        print("Let's play again!")
    elif myhand == 2 and computerpick ==1:
        print("You threw Paper and beat the Rock of the computer")
        print("Let's play again!")
    elif myhand == 3 and computerpick ==2:
        print("You threw Scissors and beat the Paper of the computer")
        print("Let's play again!")
    
