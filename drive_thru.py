#to create mcd drive thru

#defining a function to welcome the user
def welcome():
    print("Welcome to MCD Drive Thru!!")
    print("The options are:")
    print("1. Chicken Burger 🍔")
    print("2. Fries 🍟")
    print("3. Coke 🥤")
    print("4. Ice Cream 🍦")
    print("5. Cookies 🍪")
    print("Please select your item by entering the number")

#calling the function
welcome()

#taking input from the user
order = int(input("What would you like to have: "))

#defining a function to get the item
def get_item():
    if order == 1:
        return "Cheese Burger 🍔"
    elif order == 2:
        return "Fries 🍟"
    elif order == 3:
        return "Coke 🥤"
    elif order == 4:
        return "Ice Cream 🍦"
    elif order == 5:
        return "Cookies 🍪"
    else:
        return "Invalid order"
    

#calling the fn
print("Your order is: ", get_item())

"""# Drive-Thru 🚙
# Codédex

def get_item(x):
  if x == 1:
    return '🍔 Cheeseburger'
  elif x == 2:
    return '🍟 Fries'
  elif x == 3:
    return '🥤 Soda'
  elif x == 4:
    return '🍦 Ice Cream'
  elif x == 5:
    return '🍪 Cookie'
  else:
    return "invalid option"

def welcome():
  print('Welcome to Sonnyboy\'s Diner!')
  print('Here\'s the menu:')
  print('1. 🍔 Cheeseburger')
  print('2. 🍟 Fries')
  print('3. 🥤 Soda')
  print('4. 🍦 Ice Cream')
  print('5. 🍪 Cookie')

welcome()

option = int(input('What would you like to order? '))
print(get_item(option)) """
