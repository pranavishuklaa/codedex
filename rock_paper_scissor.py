#rock paper scissor adv game 

#importing module 
import random

#intrdocution to the game
print("Welcome to the Rock, Paper, Scissors Lizard Spock game!")
print("As you have already played the rock, paper, scissor game, this is an advanced version of it")

#choices for the user
print("1) Rock ✊")
print("2) Paper 🖐️")
print("3) Scissors ✌️")
print("4) Lizard 🦎")
print("5) Spock 🖖")

#usr input
choice = int(input("Enter your number: "))

#output
print("Your choice:", choice)

random_choice = random.randint(1, 5)

print(f"CPU's choice: {random_choice} ")

#conditions
if choice == 1:
    if random_choice == 1:
        print("Its a tie!")
    elif random_choice == 2:
        print("Paper covers Rock. You lose!")
    elif random_choice == 3:
        print("Rock crushes Scissors. You win!")
    elif random_choice == 4:
        print("Rock crushes Lizard. You win!")
    elif random_choice == 5:
        print("Spock vaporizes Rock. You lose!")

#2nd choice condition
elif choice == 2:
    if random_choice == 1:
        print("Paper covers Rock. You win!")
    elif random_choice == 2:
        print("Its a tie!")
    elif random_choice == 3:
        print("Scissors cuts Paper. You lose!")
    elif random_choice == 4:
        print("Lizard eats Paper. You lose!")
    elif random_choice == 5:
        print("Paper disproves Spock. You win!")

#3rd choice condition
elif choice == 3:
    if random_choice  == 1:
        print("Rock breaks Scissors. You lose!")
    elif random_choice == 2:
        print("Scissors cuts Paper. You win!") 
    elif random_choice == 3:
        print("Its a tie!")
    elif random_choice == 4:
        print("Scissors beats Liazards. You win!")
    elif random_choice == 5:
        print("Spock smashes Scissors. You lose!")

#4th choice condition
elif choice == 5:
    if random_choice == 1:
        print("Spock vaparizes Rock. You win!")
    elif random_choice == 2:
        print("Paper disproves Spock. You lose!")
    elif random_choice == 3:
        print("Spock smashes Scissors. You win!")
    elif random_choice == 4:
        print("Lizard poisons Spock. You lose!")
    elif random_choice == 5:  
        print("Its a tie!")

#5th choice condition
elif choice == 4:
    if random_choice == 1:
        print("Rock crushes Lizard. You lose!")
    elif random_choice == 2:
        print("Lizard eats Paper. You win!")
    elif random_choice == 3:
        print("Scissors beats Lizard. You lose!")
    elif random_choice == 4:
        print("Its a tie!")
    elif random_choice == 5:
        print("Lizard poisons Spock. You win!")

else: 
    print("Invalid choice!")

print("Thank you for playing the game 🫶")

        
    





