import random


player_health = 100
player_money = 50


def display_status():
    print(f"Health: {player_health}")
    print(f"Money: {player_money}")


def bar_scene():
    global player_money
    global player_health
    print("\nYou enter 'Stardust Saloon,' a bustling space bar with neon lights and alien patrons.")
    print("The bartender nods at you. What will you do?")
    print("1. Order a drink (Cost: 10 money, Restores 20 health)")
    print("2. Talk to the bartender")
    print("3. Challenge an alien to a battle (Cost: 25 money, Win: 50 money)")
    print("4. Leave the bar")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        if player_money >= 10:
            player_money -= 10
            player_health += 20
            if player_health > 100:
                player_health = 100
            print("\nYou order a drink and feel refreshed.")
        else:
            print("\nYou don't have enough money to order a drink.")
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
            print (f"\nYou lost some health after that battle. Your current health: {player_health}.")    
        else:
            print("\nYou don't have enough money to play cards.")
    elif choice == "4":
        print("\nYou leave the bar and continue your adventure.")
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
        print("\nInvalid choice. Please choose a valid option.")


if player_health <= 0:
    print("\nYour adventure ends here. You have run out of health. Better luck next time!")
