from random import randint
def start_game():
    print("**********Welcome to the number guessing game!**********")
    solution = randint(1,10)
    correctAnswer = False
    totalGuesses = 0
    highScore = 0
    print("The high score is {}".format(highScore))
    while correctAnswer == False:
        try:
            userGuess = int(input("Pick a number between 1 and 10. "))
            totalGuesses += 1
            if userGuess > 10 or userGuess < 1:
                print("Whoopsies, you can only pick a number between 1 and 10!")
            else:
                if userGuess == solution:
                    print("You did it! Game over!")
                    print("It took you {} guesses to get it right!".format(totalGuesses))
                    correctAnswer = True
                    playAgain = input("Would you like to play again? YES or NO? ").lower()
                    if highScore > totalGuesses or highScore == 0:
                        highScore = totalGuesses
                    if playAgain == 'yes':
                        print("The high score is {}".format(highScore))
                        correctAnswer = False
                        solution = randint(1,10)
                        totalGuesses = 0
                    elif playAgain == 'no':
                        correctAnswer = True
                        print("Goodbye")
                    else:
                        correctAnswer = True
                        print("Invalid response, goodbye")
                elif userGuess > solution:
                    print("Try again, the number is lower than {}.".format(userGuess))
                elif userGuess < solution:
                    print("Try again, the number is higher than {}.".format(userGuess))
        except ValueError:
            print("Woah, playa. Enter numbers only!")
    
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()