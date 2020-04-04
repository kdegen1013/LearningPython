import random

mynumber = random.randint(1, 20)
correctanswer = False


while correctanswer == False:
    myguess = int(input("What is your guess: ").strip())
    if mynumber == myguess:
        print("You guessed correctly. The number was {}".format(mynumber))
        break
    elif mynumber > myguess:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
