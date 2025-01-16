""""
A space-based adventure of a crew of curious individuals exploring an unknown galaxy.
A “Day in the Life” story that walks you through choices the main character makes based on conditions like the time of day, the actions that the player take, etc.
A classic mini-RPG (role-playing game) with hp health points, character moves like attack/block/heal, and NPCs (non-player characters) that attacks based on a random number generator.
"""

#Day in the Life

print("Welcome to the Day in the Life game!")
x = input("What is your name? ")
print(f"Hello, {x}! You are a student at a university. You wake up in the morning and have to get ready for class. What do you do? Choose your option:")
print("A. Get up and get ready for class.")
print("B. Sleep in and skip class.")
choice = input("Enter your choice: ")
if choice == "A":
    print("You get up and get ready for class. You make it to class on time and have a great day!")
elif choice == "B":
    print("You sleep in and skip class. You miss an important lecture and fall behind in your studies.")
else:
    print("None of the above")

print("Now it's time for lunch. What would you eat? Choose your option:")
print("A. Salad")
print("B. Pizza")
print("C. Sandwich")
print("D. Sushi")   
food = input("Enter your choice: ")
if food == "A":
    print("You eat a salad and feel healthy and energized.")
elif food == "B":
    print("You eat pizza and feel full and satisfied.")
elif food == "C":
    print("You eat a sandwich and feel light and refreshed.")
elif food == "D":
    print("You eat sushi and feel exotic and adventurous.")
else:
    print("None of the above")

print("After lunch, you have a few hours of free time. What do you do? Choose your option:")
print("A. Go for a walk in the park.")
print("B. Watch a movie at home.")
print("C. Meet up with friends for coffee.")
print("D. Read a book at the library.")

activity = input("Enter your choice: ")
if activity == "A":
    print("You go for a walk in the park and enjoy the fresh air and nature.")
elif activity == "B":
    print("You watch a movie at home and relax on the couch.")
elif activity == "C":
    print("You meet up with friends for coffee and have a great time catching up.")
elif activity == "D":
    print("You read a book at the library and get lost in the story.")
else:
    print("None of the above")

print("It's time for dinner. What would you like to eat? Choose your option:")
print("A. Pasta")
print("B. Steak")
print("C. Tacos")
print("D. Dal and rice")

dinner = input("Enter your choice: ")
if dinner == "A":
    print("You eat pasta and feel satisfied and content.")
elif dinner == "B":
    print("You eat steak and feel full and happy.")
elif dinner == "C":
    print("You eat tacos and feel spicy and adventurous.")
elif dinner == "D":
    print("You eat dal and rice and feel warm and comforted.")
else:
    print("None of the above")

print

