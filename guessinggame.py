import random


def get_int(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping and
    prompting the user, until a valid `int`'` is selected.
    :param prompt: The string that the user will see, when
        they're prompted to enter the value.
    :return: The integer the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        #else:
        print("{0} is not a valid number".format(temp))

help(get_int)


highest=1000
answer=random.randint(1,highest)
 #TODO: remove after testing
guess=0
print("Please guess a number between 1 and {}: ".format(highest))


while guess != answer:
    guess=get_int(": ")
    if guess==0:
        print("Game over the number was {}.".format(answer))
        break
    if guess == answer:
        print("Well done, you guessed it!")
        break

    else:
        if guess < answer:
            print("Please guess higher. (Give Up? 0 ends the game)")
        else:
            print("Please guess lower. (Give Up? 0 ends the game)")