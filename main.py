# ********************************************* START HERE  *************************************************/
#import
import random

#var
computer_resualt = 0
user_resualt = 0
winner = None

#first print
rules = int(input("Do you want to play or read the rules ? \n " +" (1) play  (2) read rules \nchoose a number :  "))
if (rules == 1):
    print("Let's play !")
else:
    print("\n Scissors cuts paper."
          "\n Paper covers rock."
          "\n Rock crushes Scissors."
          "\n { Win in three rounds }")
    print("Let's play !")

while True:

    user = int(input("(1).Rock  (2).Paper  (3).Scissors \nchoose a number : "))
    print(" \n____________________________________________________________________")

    while user > 3 or user < 1:
        user = int(input("enter valid input: "))

    if user == 1:
        user_choice = 'Rock'
    elif user == 2:
        user_choice = 'paper'
    else:
        user_choice = 'scissor'


    print("<> User choice is : " + user_choice + " <>")

    computer_choice = random.randint(1, 3)


    while computer_choice == user:
        computer_choice = random.randint(1, 3)

    if computer_choice == 1:
        computer_choice_name = 'Rock'
    elif computer_choice == 2:
        computer_choice_name = 'paper'
    else:
        computer_choice_name = 'scissor'

    print("<> Computer choice is : " + computer_choice_name + " <>")


    if ((user == 1 and computer_choice == 2) or
            (user == 2 and computer_choice == 1)):
        print("** paper Win! **")
        winner = "paper"

    elif ((user == 1 and computer_choice == 3) or
          (user == 3 and computer_choice == 1)):
        print("** Rock Win! **")
        winner = "Rock"
    else:
        print("** paper Win! **")
        winner = "paper"

    if winner == user_choice:
        print("== User wins ==")
        print("____________________________________________________________________\n")
        user_resualt += 1
    else:
        print("== Computer wins ==")
        print("____________________________________________________________________\n")
        computer_resualt += 1
    print("******~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~******")
    print(" Resultat : Computer " , str(computer_resualt)  , " User " + str(user_resualt) )
    print("******~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~******")
    if (user_resualt == 3 ):
        print(" User Winner ")
        break
    elif (computer_resualt == 3):
        print(" Computer Winner ")
        break

print("~~ Thanks For playing ّ~~")