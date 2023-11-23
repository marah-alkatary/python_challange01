import random
print("Welcome to Mystery Word!")
def word_game():
    word_list = ["red", "tomato", "chocolate", "apple", "cat", "money", "car", "book", "egg", "yellow", "salad", "juice", "cake"]
    word_to_guess = random.choice(word_list)
    number_of_attempts = 3

    print("Clues:")
    print(f"the number of letters: {len(word_to_guess)} ")
    print(f"the first letter is '{word_to_guess[0]}'.")
    print(f"the last letter is '{word_to_guess[-1]}'.")


    while number_of_attempts > 0 :
        user_guessed_word = input("Guess the word: ")
        print(f"number_of_attempts: {number_of_attempts}")
        number_of_attempts -= 1

        if  user_guessed_word == word_to_guess:
            print(f"Congratulations! You guessed the word ")
            break

        elif user_guessed_word != word_to_guess:
            print("Incorrect! Try again.")
            print(f"number_of_attempts: {number_of_attempts}")

        else :
            number_of_attempts == 0
            print(f"Sorry, you're out of attempts, The correct word \"{word_to_guess}\".")



word_game()
check_play = True
while check_play:
    play_again = input("If you like to play again choose yes or no")
    if play_again == "yes":
        word_game()
    else:
        check_play = False
        print("Good bye! ")

