import random

# Functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def instructions():
    print()
    print("**** How to play ****")
    print()
    print("Choose a starting balance ($1 min, $10 Max)")
    print()
    print("Each round costs $1")
    print("Press enter to play each round")
    print()
    print("Payout rates for each token")
    print()
    print("Unicorn increase by $4 ")
    print("Donkey decrease by $1")
    print("Zebra decrease by $0.5")
    print("Horse decrease by $0.5")
    return ""


def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # if the amount is too low / high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main Routine goes here...
statement_generator("Welcome to the Lucky Unicorn Game","#")
show_instructions = yes_no("Have you played the game before? ")

if show_instructions == "no":
    instructions()

print("")

# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with?", 0, 10)
print()
print("You will be spending ${}".format(how_much))

balance = how_much

rounds_played = 0

play_again = input("Press <enter> to play. . .").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print("*** Round #{} ***".format(rounds_played))
    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "Unicorn"
        prize_decoration = "!"
        balance += 4

    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "Donkey"
        prize_decoration = "D"
        balance -= 1

    # The token is either a horse or zebra...
    # in both cases, subtract $0.50 from the balance
    else:
        # if the number is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            prize_decoration = "H"
            chosen = "Horse"

        # otherwise set it to a zebra
        else:
            chosen = "Zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = "You got a {}. Your balance is ${:.2f}".format(chosen, balance)
    statement_generator(outcome, prize_decoration)
    if balance < 1:
        # If balance is to low, exit the game and
        # output a suitable message
        play_again = "xxx"
        print("sorry you have run out of money to play with")
    else:
        play_again = input("Press enter to play again or 'xxx' to quit")
statement_generator("Congratulations, you've got: ${:.2f}".format(balance), "=")


