
wizard = "Wizard",
elf = "Elf",
human = "Human",
master = "Sorcerer"
dragon = "Dragon"


wizard_hp = 70
elf_hp = 100
human_hp = 150
master_hp = 200
dragon_hp = 300

wizard_atk = 150
elf_atk = 100
human_atk = 20
master_atk = 200
dragon_atk = 50

print("1) Wizard\n2) Elf\n3) Human\n4) Sorcer\n5) Exit")
while True:
    character = input("Choose your character: ")
    if character == "1" or "Wizard".casefold():
        print("You chose the Wizard:")
        my_hp = wizard_hp
        print("Health: ", my_hp)
        my_atk = wizard_atk
        print("Damage: ", my_atk)
        break

    elif character == "2" or "elf".casefold():
        print("You chose the Elf")
        my_hp = elf_hp
        print("Health: ", my_hp)
        my_atk = elf_atk
        print("Damage: ", my_atk)
        break
    elif character == "3" or "human".casefold():
        print("You chose the Human")
        my_hp = human_hp
        print("Health: ", my_hp)
        my_atk = human_atk
        print("Damage: ", my_atk)
        break
    elif character == "4" or "sorcerer".casefold():
        print("You chose the Sorcerer.")
        my_hp = master_hp
        print("Health: ", my_hp)
        my_atk = master_atk
        print("Damage: ", master_atk)
        break
    elif character == "5":
        print("Thanks for playing")
        break
    else:
        print("Unknown Choice")
        continue
        print(input)

while True:
    remaining_dragon_hp = dragon_hp - my_atk
    print("The", character, "attacks the dragon!")
    print("The dragon has", remaining_dragon_hp, "left.")
    break
