# Lot's of help from https://www.youtube.com/watch?v=m4nEnsavl6w
# https://github.com/kiteco/python-youtube-code/tree/master/build-hangman-in-python

import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print("There are {} letters in your word. {}".format(len(word), word_completion))
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter {}".format(guess))
            elif guess in word:
                print("Yes, {} is in the word".format(guess))
                guessed_letters.append(guess)
                # Need to update word_complete???
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                    guess = word
            else:
                print("Wrong!")
                tries -= 1
                guessed_letters.append(guess)
        elif len(guess) == len(word):
            if guess == word:
                word_completion = guess
                guessed = True
            else:
                if guess in guessed_words:
                    print("You already guessed that word {}".format(guess))
                else:
                    print("Wrong! {} is not the word".format(guess))
                    tries -= 1
                    guessed_words.append(guess)
        else:
            print("Not a valid guess. Try again.")

        if not guessed:
            print(display_hangman(tries))
            print("Guessed Letters:")
            print(guessed_letters)
            print("Guessed Words:")
            print(guessed_words)
            print("Your Word:")
            print(word_completion)
        else:
            print("You win!")
            print("The word was {}".format(guess))


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    # Get a word for our game
    word = get_word()
    # Let's Play
    play(word)
    # After the 1st game ends, ask if they want to play again
    #
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
