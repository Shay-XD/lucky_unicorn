

# functions go here...
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
            print("please answer yes / no")



def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


# Main Routine goes here...
show_instructions = yes_no ("have you played the game before? ")

if show_instructions == "no":
    instructions()

print("Program continues")
