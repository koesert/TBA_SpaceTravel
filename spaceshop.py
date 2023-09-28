shop_items = {
    "Laser Blaster": {"price": 100, "quantity": 10},
    "Rocket Launcher": {"price": 250, "quantity": 5},
    "Pistol": {"price": 50, "quantity": 20},
    "Medkit": {"price": 30, "quantity": 15},
    "Alien Artifact": {"price": 200, "quantity": 8},
    "Upgraded Spacesuit": {"price": 300, "quantity": 3},
}

player_money = 500

def display_shop():
    print("\nWelcome to the Space Shop!")
    print("Available Items:")
    for item, details in shop_items.items():
        print(f"{item} - Price: {details['price']} Money - Quantity: {details['quantity']}")
    print(f"\nYour Money: {player_money} Money")


def shop():
    global player_money
    while True:
        display_shop()
        choice = input("\nEnter the item you want to buy (or 'exit' to leave the shop): ").capitalize()

        if choice == "Exit":
            break

        if choice in shop_items:
            item = shop_items[choice]
            if player_money >= item["price"] and item["quantity"] > 0:
                player_money -= item["price"]
                item["quantity"] -= 1
                print(f"\nYou purchased {choice}!")
            elif player_money < item["price"]:
                print("\nYou don't have enough money to buy this item.")
            else:
                print("\nSorry, this item is out of stock.")
        else:
            print("\nInvalid choice. Please choose an available item.")

if __name__ == "__main__":
    print("Welcome to the Spaceshop!")
    print("You are now in a space station with a space shop.")
    
    while True:
        print("\nOptions:")
        print("1. Go to the Space Shop")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            shop()
        elif choice == "2":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
