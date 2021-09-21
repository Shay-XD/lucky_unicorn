
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


#main routine goes here
statement_generator("Welcome to the lucky Unicorn Game", "*")
print()
statement_generator("congratulations you got a Unicorn", "!")
