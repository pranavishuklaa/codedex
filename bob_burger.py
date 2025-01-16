#objects

#creating a class

#creation of objects
from restraunts import Restaurant


Bobs_burger = Restaurant()

#assigning values to the objects
Bobs_burger.name = "Bob\'s Burgers"
Bobs_burger.category = "American Dinner"
Bobs_burger.rating = 4.7
Bobs_burger.delivery = False

#displaying the objects
print(vars(Bobs_burger))
