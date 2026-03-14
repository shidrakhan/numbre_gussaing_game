import random
answer = {'a': 1, 'b': 10}

EASSY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# funtion to check user gusss to actual answer


def check_answer(user_guees, actual_answer):
    if user_guees > actual_answer:
        print("too high.")
    elif user_guees < actual_answer:
        print("too low.")
    else:
        print(f"you got it! the answer was {actual_answer}")

# funtion to set dificulty


def set_deficulty():
    level = input("choose dificulty type 'eassy' or 'hard':")
    if level == "eassy":
        level = EASSY_LEVEL_TURNS
    else:
        level = HARD_LEVEL_TURNS


# choosing random number between 1 nd
print("welcom to the number gussing game!")
print("i am thinking of the number between 1 and 100")
answer = {'a': 1, 'b': 1}

# let the number guees by user
guees = int(input("make a guees:"))
turns = set_deficulty()
print(f"you have{turns}attempts remaning the gueees number.")


# track the number of trunsand reduce by if they get it wrong

# repeat the gussing funtionality if they get wrong
