#Chinese lucky phrase in numbers

import random

 #random choice generation
random_choice = random.randint(1, 8)

#defining the function
def fortune(): 
    random_choice = random.randint(1, 8)
    if random_choice == 1:
        print("Don't pursue happiness - create it.")
    elif random_choice == 2:
        print("All things are difficult before they are easy.")
    elif random_choice == 3:
        print("The early bird gets the worm, but the second mouse gets the cheese.")
    elif random_choice == 4:
        print("Someone in your life needs a letter from you.")
    elif random_choice == 5:
        print("Don't just think. Act!")
    elif random_choice == 6:
        print("Your heart will skip a beat.")
    elif random_choice == 7:
        print("The fortune you search for is in another cookie.")
    elif random_choice == 8:
        print("Help! I'm being held prisoner in a Chinese bakery!")
    else:
        print("Invalid choice")


#output
print("Your fortune says: ")
fortune()
fortune()
fortune()






 

 