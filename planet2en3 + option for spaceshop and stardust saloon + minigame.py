import random
import time

# Initialize the player's inventory as a global list
player_inventory = []

def establish_base_camp(planet_name):
    print(f"You establish a base camp on the alien planet {planet_name}.")
    print(f"Now, it's time to explore {planet_name}.")

def explore_nebulorion():
    print("As you venture into Nebulorion's otherworldly terrain, you come across mysterious structures.")
    time.sleep(2)
    print("These structures emit an eerie, captivating glow.")
    time.sleep(2)
    choice = input("Do you want to investigate the structures? (Yes/No): ").lower()
    if choice == "yes":
        print("You approach the structures and discover ancient alien artifacts.")
        time.sleep(2)
        print("These artifacts could be of great value.")
        return True
    else:
        print("You decide to continue exploring without investigating the structures.")
        return False

def gather_resources():
    print("While exploring, you also gather vital resources for survival.")
    inventory = []  # Initialize the player's inventory
    return inventory

def encounter_alien_fauna():
    print("As you explore, you encounter exotic alien creatures.")
    time.sleep(2)
    print("Some are docile, while others seem dangerous.")

def observe_and_interact(inventory):
    print("You decide to observe and interact with the alien creatures.")
    time.sleep(2)
    print("This could provide valuable insights.")
    time.sleep(2)
    choice = input("Do you want to interact with the creatures? (Yes/No): ").lower()
    if choice == "yes":
        print("You cautiously approach the creatures and observe their behavior.")
        time.sleep(2)
        print("You gain valuable knowledge about the planet's ecosystem.")
    else:
        print("You choose not to interact with the creatures.")

def tell_myths_and_backstory():
    print("During your time on Nebulorion, you hear myths and legends from the indigenous alien inhabitants.")
    time.sleep(2)
    print("They speak of a powerful being known as Xelthorin, the 'Scourge of the Cosmos'.")
    time.sleep(2)
    print("Xelthorin is said to have conquered numerous alien worlds, leaving destruction in his wake.")
    time.sleep(2)
    print("Many have tried to stand against him, but none have succeeded.")
    time.sleep(2)
    print("As you listen to these stories, a burning desire for vengeance grows within you.")

def alien_boss_battle(player_inventory):
    print(f"\nYour journey on the alien planet Celesterra has been filled with challenges and discoveries.")
    time.sleep(2)
    print(f"But now, you face your most formidable challenge yet.")
    time.sleep(2)
    print(f"Deep within the heart of the planet Celesterra, you discover an ancient alien citadel.")
    time.sleep(2)
    print("As you enter the citadel, you are confronted by the king of all aliens, Xelthorin!")

    # Initialize player and boss HP
    player_hp = 100
    boss_hp = 200
    
    while True:  # Allow the player to retry the battle if they are defeated
        print(f"\nYour HP: {player_hp}")
        print(f"Xelthorin's HP: {boss_hp}")
        
        action = input("Choose an item to use in the battle (or type 'fight' to attack without items): ").lower()
        
        if action == "fight":
            # Player attacks the boss
            boss_hp -= 20  # Assume the player's attack deals 20 damage
            player_hp -= 10  # Player loses 10 HP per attack
            
            if boss_hp <= 0:
                print(f"You have defeated Xelthorin on the planet Celesterra! Congratulations!")
                break
            elif player_hp <= 0:
                retry = input(f"Xelthorin has defeated you on the planet Celesterra. Do you want to retry the battle with your previous items? (Yes/No): ").lower()
                if retry == "yes":
                    # Reset player and boss HP for a retry
                    player_hp = 100
                    boss_hp = 200
                    continue
                else:
                    print(f"Your journey on the planet Celesterra ends in defeat.")
                    break
            
            print("You engage Xelthorin in combat with your bare hands.")
            
        elif action in player_inventory:
            # Player uses an item
            item_damage = random.randint(10, 30)  # Random damage between 10 and 30
            boss_hp -= item_damage
            player_hp -= 10  # Player loses 10 HP per attack
            
            if boss_hp <= 0:
                print(f"You have defeated Xelthorin on the planet Celesterra! Congratulations!")
                break
            elif player_hp <= 0:
                retry = input(f"Xelthorin has defeated you on the planet Celesterra. Do you want to retry the battle with your previous items? (Yes/No): ").lower()
                if retry == "yes":
                    # Reset player and boss HP for a retry
                    player_hp = 100
                    boss_hp = 200
                    continue
                else:
                    print(f"Your journey on the planet Celesterra ends in defeat.")
                    break
            
            print(f"You use the {action} against Xelthorin on the planet Celesterra, dealing {item_damage} damage.")
            player_inventory.remove(action)  # Remove the used item from the inventory
        
        else:
            print("Invalid choice. Please choose an item from your inventory.")
        
    # End the game on the current planet
    print(f"\nYour journey on the planet Celesterra has come to an end.")
    return player_inventory

def transition_to_next_planet(current_planet_name, next_planet_name):
    print(f"\nYour journey now takes you to the second alien planet, {next_planet_name}.")
    print(f"You bid farewell to {current_planet_name} and embark on a new adventure on {next_planet_name}.")

def explore_celesterra():
    print("As you arrive on Celesterra, you find yourself in a lush, vibrant jungle teeming with alien flora.")
    time.sleep(2)
    print("The air is thick with humidity, and strange, melodic calls echo through the canopy.")
    time.sleep(2)
    choice = input("Do you want to explore the jungle? (Yes/No): ").lower()
    if choice == "yes":
        print("You venture deeper into the jungle, discovering hidden paths and strange creatures.")
        time.sleep(2)
        print("This alien world holds many secrets waiting to be uncovered.")
        return True
    else:
        print("You decide to remain cautious and not venture into the jungle for now.")
        return False

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
    print ("But before that, you must complete this minigame to advance.")
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

shop_items = {
    "Laser blaster": {"price": 100, "quantity": 10},
    "Rocket launcher": {"price": 250, "quantity": 5},
    "Pistol": {"price": 50, "quantity": 20},
    "Medkit": {"price": 30, "quantity": 15},
    "Alien artifact": {"price": 200, "quantity": 8},
}


player_money = 100

def display_inventory():
    print("\nYour Inventory:")
    for item in player_inventory:
        print(item)


def display_spaceshop():
    global player_money  
    print("\nWelcome to the Space Shop!")
    print("Available Items:")
    for item, details in shop_items.items():
        print(f"{item} - Price: {details['price']} Money - Quantity: {details['quantity']}")
    print(f"\nYour Money: {player_money} Money")


def trade():
    global player_money, player_inventory 
    while True:
        display_spaceshop()
        display_inventory()
        choice = input("\nEnter the item you want to trade ('exit' to leave the shop or 'buy' to buy an item): ").capitalize()
        print (choice)

        if choice == "Exit":
            break

        if choice == "Buy":
            shop()

        if choice in player_inventory:
            item = choice
            player_money += shop_items[item]["price"]
            player_inventory.remove(item)
            print(f"\nYou traded {item} for {shop_items[item]['price']} Money!")
        else:
            print("\nInvalid choice. Please choose an item from your inventory.")


def shop():
    global player_money, player_inventory 
    while True:
        display_spaceshop()
        choice = input("\nEnter the item you want to buy ('exit' to leave the shop or 'trade' to trade an item): ").capitalize()
        print (choice)
        if choice == "Exit":
            break

        if choice == "Trade":
            trade()

        if choice in shop_items:
            item = shop_items[choice]
            if player_money >= item["price"] and item["quantity"] > 0:
                player_money -= item["price"]
                player_inventory.append(choice)
                item["quantity"] -= 1
                print(f"\nYou purchased {choice}!")
            elif player_money < item["price"]:
                print("\nYou don't have enough money to buy this item.")
            else:
                print("\nSorry, this item is out of stock.")
        else:
            print("\nInvalid choice. Please choose an available item.")

def spaceshop():
    print("Welcome to the SpaceShop!")
    
    while True:
        print("\nOptions:")
        print("1. Go to the Space Shop")
        print("2. Trade with the Shop")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            shop()
        elif choice == "2":
            trade()
        elif choice == "3":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

drinks_list = {
    "Stellar mojito": {"price": 15, "health_recovered": 25},
    "Nebula colada": {"price": 12, "health_recovered": 20},
    "Cosmic martini": {"price": 18, "health_recovered": 30},
    "Galactic espresso": {"price": 20, "health_recovered": 35},
    "Astronomint julep": {"price": 25, "health_recovered": 40},
    "Interstellar ipa": {"price": 22, "health_recovered": 37},
    "Quasar smoothie": {"price": 14, "health_recovered": 22},
    "Orion old fashioned": {"price": 17, "health_recovered": 28},
    "Supernova cappuccino": {"price": 16, "health_recovered": 26},
    "Galaxy lemonade": {"price": 30, "health_recovered": 50},
}

def display_shop():
    global player_money  
    print("\nWelcome to the Stardust Saloon!")
    print("Available Items:")
    for item, details in drinks_list.items():
        print(f"{item} - Price: {details['price']} Money - Health: {details['health_recovered']}")
    print(f"\nYour Money: {player_money} Money")

def display_status():
    print(f"Health: {player_health}")
    print(f"Money: {player_money}")

def bar_scene():
    global player_money
    global player_health
    print("\nYou enter 'Stardust Saloon,' a bustling space bar with neon lights and alien patrons.")
    print("The bartender nods at you. What will you do?")
    
    while True: 
        print("1. Order a drink (Cost: Varies, Restores health)")
        print("2. Talk to the bartender")
        print("3. Challenge an alien to a battle (Cost: 25 money, Win: 50 money)")
        print("4. Leave the bar")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            display_shop()
            drink_choice = input("What drink would you like to order? ").capitalize()
            if drink_choice in drinks_list:
                item = drinks_list[drink_choice]
                if player_money >= item["price"]:
                    player_money -= item["price"]
                    player_health += item["health_recovered"]
                    if player_health > 100:
                        player_health = 100
                    print(f"\nYou purchased {drink_choice} and restored {item['health_recovered']} health!")
                    break  
                else:
                    print("\nYou don't have enough money to buy this drink.")
            else:
                print("\nInvalid drink choice.")
        elif choice == "2":
            print("\nThe bartender shares stories of space adventures and alien encounters.")
        elif choice == "3":
            if player_money >= 25:
                player_money -= 25
                result = random.choice(["win", "lose"])
                if result == "win":
                    player_money += 50
                    print("\nYou challenge an alien to a battle and win! You earn 50 money.")
                else:
                    print("\nLuck is not on your side. You lose the battle.")
                    player_health -= 30
                    if player_health <= 0:
                        print("\nYou lost some health after that battle, and you have run out of health. Better luck next time!")
                    else:
                        print(f"\nYou lost some health after that battle. Your current health: {player_health}.")
                break  
            else:
                print("\nYou don't have enough money to challenge an alien.")
        elif choice == "4":
            print("\nYou leave the bar and continue your adventure.")
            break  
        else:
            print("\nInvalid choice. Please choose a valid option.")

def main():
    global player_inventory
    print("Welcome to 'Journey to the Alien Planets'!")

    # Start the game on Nebulorion
    planet_name = "Nebulorion"
    establish_base_camp(planet_name)

    # Explore Nebulorion
    artifact_found = explore_nebulorion()

    if artifact_found:
        print("You've discovered valuable ancient artifacts in Nebulorion.")
        print("These artifacts may come in handy on your journey.")
        player_inventory.append("Ancient Artifacts")

    # Gather resources on Nebulorion
    player_inventory.extend(gather_resources())

    # Continue Exploring on Nebulorion
    continue_exploring = input("Do you want to continue exploring Nebulorion? (Yes/No): ").lower()
    if continue_exploring == "yes":
        gather_resources()
        tell_myths_and_backstory()
    else:
        tell_myths_and_backstory()
        print("You decide to leave Nebulorion and head to Celesterra.")

    print ("Before heading off to the final planet of the game, being ready is key. Would you like to visit the spaceshop or Stardust Saloon once more before heading off? (it will be important for the final battle in the game.)")
    choice = input("'1' for SpaceShop, '2' for Stardust Saloon and '3' to continue to the next planet.")

    if choice == "1":
        spaceshop()
    elif choice == "2":
        bar_scene()

    random_minigame()

    # Transition to Celesterra
    transition_to_next_planet(planet_name, "Celesterra")

    # Explore Celesterra
    jungle_explored = explore_celesterra()

    if jungle_explored:
        print("You've explored the vibrant jungle of Celesterra, uncovering its secrets.")
        print("Your journey continues as you delve deeper into the alien world.")
    
    # Encounter Alien Fauna
    encounter_alien_fauna()

    # Gather Resources on Celesterra
    player_inventory.extend(gather_resources())


    # Random Minigame
    random_minigame()

    # Alien Boss Battle on Celesterra
    player_inventory = alien_boss_battle("Celesterra")

    print("Congratulations! You've completed your journey on Celesterra.")
    print("Your quest for vengeance against Xelthorin is one step closer to fulfillment.")
    print(f"You've acquired the following items on your journey: {', '.join(player_inventory)}")

if __name__ == "__main__":
    main()



