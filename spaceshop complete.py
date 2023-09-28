shop_items = {
    "Laser blaster": {"price": 100, "quantity": 10},
    "Rocket launcher": {"price": 250, "quantity": 5},
    "Pistol": {"price": 50, "quantity": 20},
    "Medkit": {"price": 30, "quantity": 15},
    "Alien artifact": {"price": 200, "quantity": 8},
}


player_money = 500
player_inventory = []


def display_inventory():
    print("\nYour Inventory:")
    for item in player_inventory:
        print(item)


def display_shop():
    global player_money  
    print("\nWelcome to the Space Shop!")
    print("Available Items:")
    for item, details in shop_items.items():
        print(f"{item} - Price: {details['price']} Money - Quantity: {details['quantity']}")
    print(f"\nYour Money: {player_money} Money")


def trade():
    global player_money, player_inventory 
    while True:
        display_shop()
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
        display_shop()
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

if __name__ == "__main__":
    print("Welcome to the Space Adventure Game!")
    print("You are now in a space station with a space shop.")
    
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
