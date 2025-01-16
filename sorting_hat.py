q1 = int(input("Do you like Dawn or Dusk? \n 1. Dawn \n 2. Dusk \n"))

Gryffindor = Ravenclaw = Hufflepuff = Slytherin = 0 # Gryffindor = 1, Ravenclaw = 2, Hufflepuff = 3, Slytherin = 4

sum = 0

if q1 == 1:
    sum = Gryffindor + 1 or Ravenclaw + 1
elif q1 == 2:
    sum = Hufflepuff + 1 or Slytherin + 1
else:
    print("Wrong input.")


total = sum

q2 = int(input("When I'm dead, I want people to remember me as: \n 1. The Good \n 2. The Great \n 3. The Wise \n 4. The Bold \n"))

if q2 == 1:
    Hufflepuff = total
    y = Hufflepuff + 2

elif q2 == 2:
    Slytherin = total
    y = Slytherin + 2

elif q2 == 3:
    Ravenclaw = total
    y = Ravenclaw + 2

elif q2 == 4:
    Gryffindor = total
    y = Gryffindor + 2

else:
    print("Wrong input.")

q3 = int(input("Which kind of instrument most pleases your ear? \n 1. The violin \n 2. The trumpet \n 3. The piano \n 4. The drum \n"))

y = total

if q3 == 1:
    Slytherin = y
    z = Slytherin + 4

elif q3 == 2:
    Hufflepuff = y
    z = Hufflepuff + 4

elif q3 == 3:
    Ravenclaw = y
    z = Ravenclaw + 4

elif q3 == 4: 
    Gryffindor = y
    z = Gryffindor + 4

else:
    print("Wrong input.")


if Gryffindor > Ravenclaw or Hufflepuff or Slytherin:
    print(" You are in Gryffindor!")

elif Ravenclaw > Gryffindor or Hufflepuff or Slytherin:
    print("You are in Ravenclaw!")

elif Hufflepuff > Gryffindor or Ravenclaw or Slytherin:
    print("You are in Hufflepuff!")

elif Slytherin > Gryffindor or Ravenclaw or Hufflepuff:
    print("You are in Slytherin!")

else:
    print("Try Again.")




    

