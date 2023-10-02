import random
def math_quiz():
    word_list = ["*", "/", "+", "-", "%"]
    word = random.choice(word_list)

    print ("Welcome to Math Quiz. Here you'll type 2 numbers and the program creates a random problem out of the 2 numbers. You must solve the problem to advance, and you have 3 attempts. Remember that your second number must be lower than your first number to prevent errors! lets get started!")
    num1 = int(input("Pick your first number:"))
    num2 = int(input("Now pick your second number (which must be lower than your first number):"))

    attempts = 3 
    while attempts > 0:
        if word == "/":
            result = int(num1 / num2)
            answer = int(input(f"{num1} {word} {num2}?"))
            print (result)
            if answer == result:
                print (f"Correct! That was {result}")
                attempts -= 4
            else: 
                print ("That was incorrect, please try again.")
                print (f"You have {attempts} attempts left")
                attempts -= 1
        elif word == "*":       
            result = int(num1 * num2)
            answer = int(input(f"{num1} {word} {num2}?"))
            print (result)
            if answer == result:
                print (f"Correct! That was {result}")
                attempts -= 4
            else: 
                print ("That was incorrect, please try again.")
                print (f"You have {attempts} attempts left")
                attempts -= 1
        elif word == "+":       
            result = int(num1 + num2)
            answer = int(input(f"{num1} {word} {num2}?"))
            print (result)
            if answer == result:
                print (f"Correct! That was {result}")
                attempts -= 4
            else: 
                print ("That was incorrect, please try again.")
                print (f"You have {attempts} attempts left")
                attempts -= 1
        elif word == "-":       
            result = int(num1 - num2)
            answer = int(input(f"{num1} {word} {num2}?"))
            print (result)
            if answer == result:
                print (f"Correct! That was {result}")
                attempts -= 4
            else: 
                print ("That was incorrect, please try again.")
                print (f"You have {attempts} attempts left")
                attempts -= 1
        elif word == "%":       
            result = int(num1 % num2)
            answer = int(input(f"{num1} {word} {num2}?"))
            print (result)
            if answer == result:
                print (f"Correct! That was {result}")
                attempts -= 4
            else: 
                print ("That was incorrect, please try again.")
                print (f"You have {attempts} attempts left")
                attempts -= 1 

    if attempts == 0:
        print(f"Sorry, you've used all your attempts. The correct answer was '{result}'.")
        


def half_word():
    word_list = ["space", "travel", "time", "planet", "alien", "ship", "weapon", "item", "survival"]
    word = random.choice(word_list)
    partial_word = word[:3]  
    remaining_letters = '_' * (len(word) - 3)


    display_word = partial_word + remaining_letters
    print("Welcome to Half word. This one's pretty simple; You'll get the first 3 letters of a word on display and based on that you’ll have to guess what the word will be. Be careful about your guesses, because you only have 3 attempts, so make them count!")
    print(f"Here are the first three letters of a word: {display_word}")


    attempts = 3
    while attempts > 0:
        user_guess = input("Complete the word: ").lower()


        if user_guess == word:
            print("Congratulations! You guessed the word correctly.")
            break
        else:
            print(f"Sorry, that's not correct. You have {attempts - 1} attempts left.")
            attempts -= 1


    if attempts == 0:
        print(f"Sorry, you've used all your attempts. The correct word was '{word}'.")


def word_jumble():
    word_list = ["space", "travel", "time", "planet", "alien", "ship", "weapon", "item", "survival"]
    word = random.choice(word_list)




    shuffled_word = list(word)
    random.shuffle(shuffled_word)
    shuffled_word = "".join(shuffled_word)


    print("Welcome to Word jumble. This one's pretty simple; You'll get a word on display but the letters in the word are shuffled. You will have to guess what the word is. Be careful about your guesses, because you only have 5 attempts, so make them count!")


    print("Here's your word:", shuffled_word)


    attempts = 5


    while attempts > 0:
        user_guess = input("Your guess: ").lower()


        if user_guess == word:
            print("Congratulations, You guessed the word! It was indeed", word)
            break
        else:
            print("Unfortunate, because that is incorrect.")
            attempts -= 1


            if attempts > 0:
                print(f"You have {attempts} attempts left.")


    if attempts == 0:
        print("You used all your attempts. The word was:", word)


def hangman():
    word_list = ["space", "travel", "time", "planet", "alien", "ship", "weapon", "item", "survival"]
    word = random.choice(word_list)


    guessed_word = ["_" for _ in range(len(word))]


    print("Welcome to Hangman. Here you’ll have to guess a word a letter at a time. The only thing you’ll get to know is how many letters the word contains. Once you type a letter which is in the word, the program will show you how far you are from guessing the word in question. Hint: All the words are related to space travel. Let’s start!")


    print("".join(guessed_word))
    print(f"Letter count is {len(word)}")


    max_attempts = 15
    attempts = 0


    while attempts < max_attempts:
        user_input = input("Guess a letter: ").lower()
        attempts += 1


        if len(user_input) == 1 and user_input.isalpha():
            if user_input in word:
                for i in range(len(word)):
                    if user_input == word[i]:
                        guessed_word[i] = user_input
            else:
                print(f"Wrong, letter '{user_input}' is not in this word")
        else:
            print("This is not a letter, try again.")


        print("".join(guessed_word))


        if "_" not in guessed_word:
            print("Congratulations! You guessed the word: " + word)
            break


    if attempts == max_attempts:
        print("You have used all your attempts, therefore you lost. The word was: ", word)


def wordle():
    word_list = ["space", "travel", "time", "planet", "alien", "ship", "weapon", "item", "survival"]
    word = random.choice(word_list)


    print("Welcome to Wordle. Here you’ll have to guess a word based on the amount of letters it contains. Once you type a word that contains the same letters, the program will show you how far you are from guessing the word in question Hint: All the words are related to space travel. Let’s start!")


    guessed_word = ["_" for _ in range(len(word))]
    print("".join(guessed_word))
    print(f"Letter count is {len(word)}")


    max_attempts = 5
    attempts = 0


    while attempts < max_attempts:
        user_input = input("What do you think the word might be?").lower()
        attempts += 1


        if user_input == word:
            print("Correct!")
            break


        for i in range(len(word)):
            if user_input[i] == word[i]:
                guessed_word[i] = user_input[i]
            elif user_input[i] in word:
                print(f"Letter '{user_input[i]}' is in the word, but in a different spot.")


        print("".join(guessed_word))


        if attempts < max_attempts:
            print(f"You have {max_attempts - attempts} attempts left.")
        else:
            print("You have used all your attempts, therefore you lost. The word was: ", word)
 
def random_minigame():
    game_list = ["1", "2", "3", "4", "5"]
    choice = random.choice(game_list)
    if choice == "1":
        math_quiz()
    elif choice == "2":
        half_word()
    elif choice == "3":
        word_jumble()
    elif choice == "4":
        hangman()
    elif choice == "5":
        wordle()


