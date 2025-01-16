height = int(input("Enter the height: "))
credits = int(input("Enter the credits: "))

if height > 137 and credits > 10:
    print("Enjoy the ride.")
elif height < 137 and credits > 10: 
    print("You're not tall enough to ride.")
elif height > 137 and credits < 10:
    print("You don't have enough credits.")
else: 
    print("You're not tall enough to ride and you don't have enough credits.")
