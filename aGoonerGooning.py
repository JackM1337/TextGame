import random

#Player stats
player_health = 100
player_hands = "Fistdacuffs"

#Inventory system
inventory = []

def add_item(item):
    inventory.append(item)
    print(f"{item} has been added to your inventory.")

def remove_item(item):
    if item in inventory:
        inventory.remove(item)
        print(f"{item} has been removed from your inventory.")
    else:
        print(f"{item} is not in your inventory.")

def view_inventory():
    if inventory:
        print("Your inventory contains:")
        for item in inventory:
            print(f"- {item}")
        else:
            print("your inventory is empty.")

while True:
    print("\nInventory Menu:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Inventory")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter item to add: ")
        add_item(item)
    elif choice == "2":
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == "3":
        view_inventory()
    elif choice == "4":
        print("Exiting the inventory menu")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4")


#Enemy stats
enemy_health = 80

#Rest mechanic
def rest(current_health, healing_amount):
    new_health = current_health + healing_amount
    if new_health > 100:
        new_health = 100
    return new_health

#Equip mechanic
def equip_weapon(player_hands, new_weapon):
    if player_hands !="": #check for equipped weapon
        #prompt the player what to do next
        equip_weapon_item = input(f"You currently have {player_hands} equipped. Do you want to equip a new weapon or rock with what you've got? (Type 'Equip a new weapon' or 'Rock with them'): ").strip().lower()

        if equip_weapon_item == "equip a new weapon":
            player_hands = new_weapon #equip the new weapon
            print(f"You have equipped the {new_weapon}.")
        elif equip_weapon_item == "rock with them":
            print(f"You're rocking the {player_hands}")
        else:
            print("That's not a choice dude, type in 'Equip a new weapon' or 'Rock with them'.")
    else:
        #if no weapon is equipped, simply equip the new one
        player_hands = new_weapon
        print("You equipped the new weapon!")


    return player_hands #Return the updated weapon
        

print("\nWelcome to your new grand adventure!")
print("What is your next move?\n")

game = input("Do you want to explore or rest?").strip().lower()

if game == "explore":
    print("\nYou wander into a clearing and encounter an enemy!\n")

    while enemy_health > 0 and player_health > 0:
        if player_health > 70:
            player_attack_move = "All your goddamn might!"
            player_attack_power = random.randint(10,15)
        elif player_health > 40:
            player_attack_move = "A solid fucking punch"
            player_attack_power = random.randint(5,15)
        else:
            player_attack_move = "A sad desperate attempt not to die"
            player_attack_power = random.randint(3,10)

        if enemy_health > 70:
            enemy_attack_move = "brutally headbutts your ass"
            enemy_attack_power = random.randint(10,20)
        elif enemy_health > 60:
            enemy_attack_move = "uses a WWE body slam"
            enemy_attack_power = random.randint(5,15)
        elif enemy_health > 50:
            enemy_attack_move = "uses a fleshlight, wtf?"
            enemy_attack_power = random.randint(5,15)
        elif enemy_health > 40:
            enemy_attack_move = "uses Pocket sand"
            enemy_attack_power = random.randint(5,15)
        elif enemy_health > 30:
            enemy_attack_move = "uses glitter"
            enemy_attack_power = random.randint(5,15)
        else:
            enemy_attack_move = "is just trying okay?"
            enemy_attack_power = random.randint(3,10)


        action = input("You standing your ground or running like a bitch? (attack/run) ").strip().lower()

        if action == "attack":
            #player attacks enemy
            enemy_health -= player_attack_power
            print(f"\nYou used {player_attack_move} The goblin's health is now {max(enemy_health, 0)}.")

            if enemy_health <= 0:
                print("You beat homies ass...\n")
                break #ends loop

            #enemy attacks player
            player_health -= enemy_attack_power
            print(f"The bitch boi goblin  {enemy_attack_move}. Your health is now {max(player_health, 0)}.\n")

            if player_health <= 0:
                print("You actually got your ass beat by a goblin bro....\n")
                break #ends loop
        elif action == "run":
            print("You succesfully bitched out from a fight with a goblin -_- nice\n")
            break
        else:
            print("Did I say that's a choice? Attack or run dude, cmon\n")


elif game == "rest":
    print("\nYou sleep nice like a good little boy")
    player_health = rest(player_health, 20)
    print(f"Your health is now {player_health}.\n")

else:
    print("\nYou sit thinking about what other goon shit to do\n")

print("You continue on being a g\n")
            
