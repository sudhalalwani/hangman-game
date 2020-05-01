import random
def hangman():
    word = random.choice(["pugger" , "littlepugger" , "tiger" , "superman" , "thor" , "pokemon" , "avengers" , "savewater" , "earth" , "annable"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turn = 10
    guessmade = ''
    while len(word) > 0:
        main = ""

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "

        print("Guess the word: ", main)
        guess = input()
        if guess in validLetters:
            guessmade = guessmade + guess

        if guess not in word:
            turn = turn - 1
            if turn == 9:
                print("----------")
                print("turns left", turn)
            if turn == 8:
                print("----------")
                print("0")
                print("turns left", turn)
            if turn == 7:
                print("----------")
                print("0")
                print("|")
                print("turns left", turn)
            if turn == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turn == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turn == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turn == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turn == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turn == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turn == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


        if main == word:
            print("you won")
            break




name = input("Enter your name: ")
print("Welcome" + name)
print("-----------------")

print("Rules:- \n1. number of attempts = 10\n2. Guess the alphabets")
print("-----------------")
hangman()
