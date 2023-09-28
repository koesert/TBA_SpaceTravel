import random
import time

has_echopluto_leadership = False
has_treasury_key = False
has_katana = False
has_repair_kit = False

def visit_treasury():
    if has_treasury_key == True:
        print("You arrive at the treasury in the kingdom and open the door with the key you found at the alien outpost.")
        time.sleep(2)
        print("You steal all valuables and leave as quickly as possible with your spaceship")
        time.sleep(2)
        print("You live long and happy with all the happiness money can buy.")
        # End Game
    else:
        print("You arrive at the treasury in the kingdom and are met with a dozen guards.")
        time.sleep(2)
        print("You try to steal all valuables and leave as quickly as possible, however the guards catch you...")
        time.sleep(2)
        print("You get thrown in jail and have to spend the rest of your life behind bars on an alien planet")
        # End Game


def meet_leader():
    print("As you explore the planet, you suddenly come face-to-face with the leader of Planet Echopluto.")
    time.sleep(2)
    print("The leader of Echopluto is a tall, imposing figure with a regal presence.")
    time.sleep(2)

    while True:
        print("What would you like to do?")
        time.sleep(2)
        print("1. Attempt to kill the leader")
        time.sleep(2)
        print("2. Greet the leader")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            kill_leader()
            break
        elif choice == "2":
            greet_leader()
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2).")

def kill_leader():
    global has_echopluto_leadership
    print("You attempt to kill the leader of Planet Echopluto...")
    time.sleep(2)
    outcome = random.choice(["start_war", "take_over_leadership"])
    if outcome == "start_war":
        print("Your attempt to kill the leader sparks a war between you and the army of Echopluto.")
        time.sleep(2)
        print("You perish in an attempt to defend yourself and will now be forever forgotten.")
        # End Game
    elif outcome == "take_over_leadership":
        print("You successfully eliminate the leader and take over leadership of Planet Echopluto.")
        time.sleep(2)
        print("As the new leader of Echopluto, you gain the ability to plan future attacks on other planets.")
        # End Game (Or play again with echopluto leadership)
        has_echopluto_leadership = True

def greet_leader():
    print("You decide to greet the leader of Planet Echopluto...")
    time.sleep(2)
    print("The leader welcomes you to the kingdom of Echopluto and introduces himself as King Zorvax.")
    time.sleep(2)
    
    while True:
        print("King Zorvax says, 'Would you like me to show you around our kingdom?'")
        time.sleep(2)
        print("1. Accept the offer and explore the kingdom with King Zorvax")
        time.sleep(2)
        print("2. Attempt to kill King Zorvax")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            explore_kingdom_with_king_zorvax()
            break
        elif choice == "2":
            kill_leader()
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2).")

def explore_kingdom_with_king_zorvax():
    print("King Zorvax takes you on a guided tour of the kingdom.")
    time.sleep(2)
    print("You are amazed by the alien architecture and the unique culture of Echopluto.")
    time.sleep(2)
    
    while True:
        print("After the tour, King Zorvax leaves you to explore the kingdom on your own.")
        time.sleep(2)
        print("What do you wish to do?")
        time.sleep(2)
        print("1. Try to steal all valuables from the treasury")
        time.sleep(2)
        print("2. Go to the throne room")
        time.sleep(2)
        print("3. Be rude and try to leave the planet")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            visit_treasury()
            break
        elif choice == "2":
            go_to_throne_room()
            break
        elif choice == "3":
            if random.random() < 0.5:
                print("You manage to escape the planet successfully with your ship.")
                # End Game
                break
            else:
                print("Your rude behavior gets you thrown in jail. Your adventure ends here.")
                # End Game
                return
        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")

def go_to_throne_room():
    print("You go to the throne room of the kingdom and see King Zorvax again.")
    time.sleep(2)
    print("King Zorvax says: 'We meet again traveller'")
    time.sleep(2)

    while True:
        print("What do you do?")
        time.sleep(2)
        print("1. Attempt to kill King Zorvax")
        time.sleep(2)
        print("2. Say: 'Hello'")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            kill_leader()
            break
        elif choice == "2":
            print("King Zorvax says: 'You dare speak to me with that tone!'")
            time.sleep(2)
            print("'Guards! Capture him and and put him in jail'")
            time.sleep(2)
            print("You end up behind bars and have to spend the rest of your life in jail.")
            # End Game
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")

def visit_alien_outpost():
    print("You make your way towards the alien outpost in the distance.")
    time.sleep(2)
    
    while True:
        print("As you approach the outpost, you are met with two choices:")
        time.sleep(2)
        print("1. Investigate the alien outpost")
        time.sleep(2)
        print("2. Keep moving to another location")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            investigate_alien_outpost()
            break
        elif choice == "2":
            print("You choose to keep exploring and leave the alien outpost behind.")
            meet_leader()
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2).")

def investigate_alien_outpost():
    global has_treasury_key
    print("You decide to investigate the alien outpost.")
    time.sleep(2)
    print("As you explore the outpost, you stumble upon a key which seems to be of significant use.")
    time.sleep(2)
    print("The key looks to be able to open the treasury that is located in the kingdom")
    time.sleep(2)
    has_treasury_key = True
    while True:
        print("You are faced with two choices:")
        time.sleep(2)
        print("1. Keep searching the alien outpost")
        time.sleep(2)
        print("2. Leave to go steal all valuables from the treasury in the kingdom")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            keep_searching_alien_outpost()
            break
        elif choice == "2":
            visit_treasury()
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2).")

def keep_searching_alien_outpost():
    print("You continue searching the alien outpost and make an astonishing discovery.")
    time.sleep(2)
    print("You find a set of keys to a secret spaceship and a map with directions to a hidden garage.")
    time.sleep(2)
    print("This could be your ticket to an incredible adventure!")
    time.sleep(2)

    while True:
        print("You are faced with three choices:")
        time.sleep(2)
        print("1. Follow the directions to the secret garage")
        time.sleep(2)
        print("2. Check upstairs in the outpost")
        time.sleep(2)
        print("3. Leave to go steal all valuables from the treasury in the kingdom")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            follow_secret_garage_directions()
            break
        elif choice == "2":
            check_upstairs_outpost()
            break
        elif choice == "3":
            visit_treasury()
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2).")

def check_upstairs_outpost():
    global has_katana
    print("You decide to check upstairs in the outpost.")
    time.sleep(2)
    print("To your surprise, you find a medkit and a razor sharp katana.")
    time.sleep(2)
    print("These items could be very useful in the future.")
    time.sleep(2)

    has_katana = True

    print("You decide to continue with your adventure by following the directions to the secret garage.")
    time.sleep(2)
    follow_secret_garage_directions()

def follow_secret_garage_directions():
    print("Following the map's directions, you arrive at the hidden garage.")
    time.sleep(2)
    print("You notice two entrances to the garage.")
    time.sleep(2)
    
    while True:
        print("You are faced with two choices:")
        time.sleep(2)
        print("1. Enter the garage via the main door")
        time.sleep(2)
        print("2. Enter the garage via the side entrance")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            enter_garage_via_main_door()
            break
        elif choice == "2":
            enter_garage_via_side_entrance()
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2).")

def enter_garage_via_main_door():
    print("You choose to enter the garage via the main door.")
    time.sleep(2)
    print("As you step inside, you come face-to-face with a small group of guards.")
    time.sleep(2)
    
    while True:
        print("You have two choices:")
        time.sleep(2)
        print("1. Try to kill the small group of guards")
        time.sleep(2)
        print("2. Greet the small group of guards and lie about being sent by their leader")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            if random.random() < 0.5:
                print("You successfully eliminate the guards and escape with the alien spaceship.")
                time.sleep(2)
                print("You live long and happy with a new alien spaceship.")
            else:
                print("Your attempt to kill the guards fails, and you are captured.")
                time.sleep(2)
                print("You are fed to alien lions and do not survive. Your adventure ends here.")
            return
        elif choice == "2":
            test_guards_with_leader_name()
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2).")

def test_guards_with_leader_name():
    print("You greet the guards and claim to have been sent by their leader.")
    time.sleep(2)
    print("The guards look skeptical and decide to test your knowledge.")
    time.sleep(2)

    alien_names = ["King Xorlon", "King Glyptor", "King Zarnak", "King Zorvax"]
    correct_leader_name = "King Zorvax"

    random.shuffle(alien_names)

    print("The guards ask, 'What is our leader's name?'")
    for i, name in enumerate(alien_names, start=1):
        time.sleep(2)
        print(f"{i}. {name}")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == str(alien_names.index(correct_leader_name) + 1):
        print("You correctly guess the leader's name. The guards believe you and let you go with the spaceship.")
        time.sleep(2)
        print("You live long and happy with a new alien spaceship.")
        # End Game
    else:
        print("Your guess is incorrect. The guards capture you and feed you to alien lions. Your adventure ends here.")
        # End Game

def enter_garage_via_side_entrance():
    print("You choose to enter the garage via the side entrance.")
    time.sleep(2)
    print("As you sneak inside, you spot a pistol lying on the ground.")
    time.sleep(2)

    pistol_name = random.choice(["Laser Blaster", "Plasma Pistol", "Ion Disruptor"])

    print(f"You pick up the {pistol_name}, a well-known alien weapon.")
    time.sleep(2)
    print("You proceed further into the garage and see the alien spaceship, but there's a guard nearby.")
    time.sleep(2)

    while True:
        global has_katana
        print("You have two choices:")
        time.sleep(2)
        print("1. Try to silently eliminate the guard")
        time.sleep(2)
        print(f"2. Execute the guard with the {pistol_name}")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            if has_katana == True:
                print("You silently eliminate the guard with the katana you found earlier. Good thing you checked upstairs")
                time.sleep(2)
                print("You steal the alien spaceship and live long and happy.")
            else:
                print("You try to kill the guards with your bare hands. You succeed but in doing so now bring the attention of other guard to you.")
                time.sleep(2)
                print("You get captured and fed to alien lions. Your adventure ends here")
                # End Game
            break
        elif choice == "2":
            print(f"You execute the guard with the {pistol_name} and can now safely steal the alien spaceship")
            time.sleep(2)
            print("You live long and happy with a new alien spaceship.")
            # End Game
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2).")

def explore_planet():
    print("As you explore the planet, you encounter strange creatures and unusual landscapes.")
    time.sleep(2)

    while True:
        print("What would you like to do?")
        time.sleep(2)
        print("1. Keep exploring the planet")
        time.sleep(2)
        print("2. Go to the alien outpost in the distance")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            print("You continue to explore the fascinating planet Echopluto.")
            time.sleep(2)
            meet_leader()
            break
        elif choice == "2":
            visit_alien_outpost()
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")

def fix_spaceship():
    global has_repair_kit
    while True:
        print("What would you like to do?")
        time.sleep(2)
        print("1. Fix your spaceship")
        time.sleep(2)
        print("2. Abandon ship and go to alien outpost")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            if has_repair_kit == True:
                print("You fix your spaceship and leave all of the mysteries of Echopluto behind")
                # End Game
                break
            else:
                print("You dont have a repair kit to fix your spaceship and decide to abandon your ship and go to the alien outpost")
                time.sleep(2)
                visit_alien_outpost()
                break
        elif choice == "2":
            visit_alien_outpost()
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")


def arrive_at_echopluto():
    print("Welcome to the Planet Echopluto Adventure!")
    time.sleep(2)
    print("You arrive with your spaceship on the planet Echopluto.")
    time.sleep(2)
    
    while True:
        print("What do you want to do?")
        time.sleep(2)
        print("1. Stay in your ship")
        time.sleep(2)
        print("2. Go outside and step foot on the planet")
        time.sleep(2)
        print("3. Go back to where you came from")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            print("You decide to stay in your ship for now.")
            time.sleep(2)
            print("That choice seems a bit boring. Please choose again.")
            time.sleep(2)
        elif choice == "2":
            print("You step outside and set foot on the mysterious planet Echopluto.")
            time.sleep(2)
            explore_planet()
            break
        elif choice == "3":
            print("You decide to go back to where you came from. Your ship gets hit with a meteor and you are now stranded on this planet")
            time.sleep(2)
            fix_spaceship()
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")

arrive_at_echopluto()