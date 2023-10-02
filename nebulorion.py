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
    inventory = []  
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


def nebulorion():
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

if __name__ == "__main__":
    nebulorion()
