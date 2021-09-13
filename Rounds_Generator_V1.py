# set balance for testing purpose
balance = 5

rounds_played = 0

play_again = input("press <enter> to play...")
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print("*** round #{} ***".format(rounds_played))
    balance -= 1
    print("balance: ", balance)
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("press enter to play again or 'xxx' to quit")

print()
print("Final balance", balance)
