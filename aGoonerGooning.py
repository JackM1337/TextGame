import random

#Player stats
player_health = 100

inventory = []


#Enemy stats
enemy_health = 100


print("\nWelcome to your new grand adventure!")
print("What is your next move?\n")

choice = input("Do you want to explore or rest?").strip().lower()

if choice == "explore":
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


elif choice == "rest":
    print("\nYou sleep nice like a good little boy")
    player_health += 20
    print(f"Your health is now {player_health}.\n")

else:
    print("\nYou sit thinking about what other goon shit to do\n")

print("You continue on being a g\n")
            
