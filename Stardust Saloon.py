import random

player_health = 100
player_money = 50

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

while player_health > 0:
    display_status()
    print("\nYou find yourself in a space station with various options:")
    print("1. Visit the bar")
    print("2. Explore the station")
    print("3. Quit")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        bar_scene()
    elif choice == "2":
        print("\nYou explore the space station, discovering new places and meeting interesting characters.")
    elif choice == "3":
        print("\nYou decide to end your adventure. Thanks for playing!")
        break
    else:
        print
