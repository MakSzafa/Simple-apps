import random

print("This is HangMan by Max\n")

listOfWords = ["glass", "calculate", "complex", "idiotic", "clean", "protective", "religion", "orange"]

rollWord = random.choice(listOfWords)

def hang(tries):
    if tries == 9:
        print("______")
    elif tries == 8:
        print("   |   ")
        print("   |   ")
        print("   |   ")
        print("   |   ")
        print("   |   ")
        print("___|___")
    elif tries == 7:
        print("_________   ")
        print("        |   ")
        print("        |   ")
        print("        |   ")
        print("        |   ")
        print("        |   ")
        print("     ___|___")
    elif tries == 6:
        print("_________   ")
        print("   |    |   ")
        print("        |   ")
        print("        |   ")
        print("        |   ")
        print("        |   ")
        print("     ___|___")
    elif tries == 5:
        print("_________   ")
        print("   |    |   ")
        print("   o    |   ")
        print("        |   ")
        print("        |   ")
        print("        |   ")
        print("     ___|___")
    elif tries == 4:
        print("_________   ")
        print("   |    |   ")
        print("   o    |   ")
        print("   |    |   ")
        print("   |    |   ")
        print("        |   ")
        print("     ___|___")
    elif tries == 3:
        print("_________   ")
        print("   |    |   ")
        print("   o    |   ")
        print("  \|    |   ")
        print("   |    |   ")
        print("        |   ")
        print("     ___|___")
    elif tries == 2:
        print("_________   ")
        print("   |    |   ")
        print("   o    |   ")
        print("  \|/   |   ")
        print("   |    |   ")
        print("        |   ")
        print("     ___|___")
    elif tries == 1:
        print("_________   ")
        print("   |    |   ")
        print("   o    |   ")
        print("  \|/   |   ")
        print("   |    |   ")
        print("  /     |   ")
        print("     ___|___")
    elif tries == 0:
        print("_________   ")
        print("   |    |   ")
        print("   o    |   ")
        print("  \|/   |   ")
        print("   |    |   ")
        print("  / \   |   ")
        print("     ___|___")
        print("You lost! ;/")

print("Your task is to guess the word in 10 tries")
print("The word has %s letters\n" % len(rollWord))
guessWordStart = "_" * len(rollWord)
print(guessWordStart, "\n")
tries = 10
guessList = []
guessList2 = []

while tries > 0:
    guessWord = ""
    print("You have %s tries left" % tries)
    guess = input("Guess a letter\n")
    if guess in guessList:
        print("You have already said this letter, try another one")
    else:
        guessList.append(guess)
        print("Guessed letters", guessList)
        if guess in rollWord:
            guessList2.append(guess)
            for letter in rollWord:
                if letter in guessList2:
                    guessWord = guessWord + letter
                else:
                    guessWord = guessWord + "_"
            guessWord2 = guessWord
            print(guessWord)
            hang(tries)
            if guessWord == rollWord:
                print("Congratulations, You won!")
                tries = 0
        elif guess not in rollWord and len(guessList2) == 0:
            print(guessWordStart)
            tries -= 1
            hang(tries)
        else:
            print(guessWord2)
            tries -= 1
            hang(tries)






