#gambling machine hehe

import random

#creation of list 

symbol = [" 🍒 ", " 🍇 "," 🍉 "," 7️⃣ "]

results = random.choices(symbol,k=3)

print(f"{'|'.join(results)}")

if results == [" 7️⃣ "," 7️⃣ "," 7️⃣ "]:
    print("Jackpot!💰")
else:
    print("Thank you for playing!")


"""
def play():

choice = input("Would you like to play? (Y/N) ")

while choice == "Y":
    results = random.choices(symbol,k=3)
    print(f"{'|'.join(results)}")

    if results == [" 7️⃣ "," 7️⃣ "," 7️⃣ "]:
        print("Jackpot!💰")
    else:
        print("Thank you for playing!")

    choice = input("Would you like to play again? (Y/N) ")

"""

