dinner_options = ["sushi",
                   "kbbq",
                   "smoked meats",
                   "pasta",
                   "pizza",
                   "Chick-Fil-A",
                   "In-n-Out",
                   "mini wantons",
                   "Costco cafe"
                   ]
#valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
valid_choices = []
for i in range(1, len(dinner_options) + 1):
    valid_choices.append(str(i))
print(valid_choices)

current_choice = " "
computer_parts = []

while current_choice!= "0":
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) -1
        chosen_part = dinner_options[index]
        computer_parts.append(chosen_part)

    else:
        print("Please add options from the list below:")
        for number, part in enumerate(dinner_options):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)