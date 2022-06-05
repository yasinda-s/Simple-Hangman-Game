def welcome():
    name = input("Please enter your name: ")
    print("Hello ", name, "! Welcome to our python built hangman game. Enjoy!")
    print("You will be given 3 turns to guess the correct word hidden in the blanks. Good luck!")
    hangman_game()

def hangman_game():
    word = 'secret' #the secret word
    turns = 3 #number of turns given to the user
    guessed = '' #keep track on what user inputted

    while len(word) > 0:
        message = "" #the message that will help the user guess

        for letter in word: #to seek each letter in the word
            if letter in guessed: #did the user guess the letter?
                message = message + letter #if so, add it to the string
            else:
                message = message + "_ " #needs to run first to get blank lines

        if message == word: #has the user fully guessed the word
            print("You guessed the secret word correctly!")
            print("The word was :", word)
            quit()

        print("Guess the word:", message)
        guess = input()
        guessed = guessed + guess

        if guess not in word: #for everytime the user guesses something wrong
            turns = turns - 1
            if turns == 2:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")

            if turns == 1:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |      \n"
                      "__|__\n")
            if turns == 0:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "__|__\n")
                print("You have failed to guess the word which was", word + ".")
                quit()

welcome()

